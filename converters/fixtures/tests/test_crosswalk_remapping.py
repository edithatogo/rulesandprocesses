from __future__ import annotations

import pytest

from pic_fixture_converters import (
    UnsupportedConstructError,
    openfisca_to_pic,
    pic_to_openfisca,
    pic_to_policyengine,
    policyengine_to_pic,
)


def _crosswalk():
    return {
        "conformsTo": "pic-crosswalk/0.1.0",
        "jurisdictionScope": {"country": "XX"},
        "provenance": {"curator": "test", "method": "mechanical", "source": "unit test"},
        "rows": [
            {
                "id": "demo/variable.salary",
                "label": "Salary",
                "kind": "variable",
                "dataType": "decimal",
                "mappings": [
                    {"system": "openfisca", "ref": "salaire", "method": "mechanical"},
                    {"system": "policyengine", "ref": "employment_income", "method": "mechanical"},
                ],
                "sourceRefs": ["unit"],
                "definition": "Example salary variable.",
            },
            {
                "id": "demo/variable.tax",
                "label": "Tax",
                "kind": "variable",
                "dataType": "decimal",
                "mappings": [
                    {"system": "openfisca", "ref": "impot", "method": "mechanical"},
                    {"system": "policyengine", "ref": "income_tax", "method": "mechanical"},
                ],
                "sourceRefs": ["unit"],
                "definition": "Example tax variable.",
            },
        ],
    }


def test_openfisca_crosswalk_maps_native_names_to_pic_ids() -> None:
    fixture = openfisca_to_pic(
        {
            "name": "Crosswalk",
            "period": "2026",
            "input": {"salaire": 1000},
            "output": {"impot": 100},
        },
        crosswalk=_crosswalk(),
    )[0]

    case = fixture["cases"][0]
    assert set(case["inputs"]) == {"demo/variable.salary"}
    assert set(case["expected"]) == {"demo/variable.tax"}
    assert pic_to_openfisca(fixture, crosswalk=_crosswalk())[0]["input"] == {"salaire": 1000}


def test_policyengine_crosswalk_maps_pic_ids_to_native_names() -> None:
    fixture = policyengine_to_pic(
        {
            "name": "Crosswalk",
            "period": "2026",
            "input": {"employment_income": 1000},
            "output": {"income_tax": 100},
        },
        crosswalk=_crosswalk(),
    )[0]

    engine_doc = pic_to_policyengine(fixture, crosswalk=_crosswalk())[0]

    assert set(fixture["cases"][0]["inputs"]) == {"demo/variable.salary"}
    assert engine_doc["input"] == {"employment_income": 1000}
    assert engine_doc["output"] == {"income_tax": 100}


def test_missing_crosswalk_mapping_raises_offending_name() -> None:
    with pytest.raises(UnsupportedConstructError, match="missing_crosswalk_mapping:unknown"):
        openfisca_to_pic(
            {
                "name": "Missing mapping",
                "period": "2026",
                "input": {"unknown": 1},
                "output": {"impot": 0},
            },
            crosswalk=_crosswalk(),
        )


def test_pic_to_engine_uses_crosswalk_without_embedded_id_map() -> None:
    fixture = {
        "conformsTo": "pic-fixtures/0.1.0",
        "provenance": {
            "curator": "test",
            "method": "mechanical",
            "source": "unit",
            "interpreterOfRecord": "unit",
            "disclaimer": "unit",
        },
        "cases": [
            {
                "caseId": "demo/case.basic",
                "description": "Basic",
                "period": "2026",
                "entities": {},
                "inputs": {
                    "demo/variable.salary": {
                        "value": 1000,
                        "valueState": "known",
                        "epistemicStatus": "observed",
                    }
                },
                "expected": {
                    "demo/variable.tax": {
                        "value": 100,
                        "valueState": "known",
                        "epistemicStatus": "asserted",
                    }
                },
                "sourceRefs": ["unit"],
            }
        ],
    }

    assert pic_to_openfisca(fixture, crosswalk=_crosswalk()) == [
        {"name": "Basic", "period": "2026", "input": {"salaire": 1000}, "output": {"impot": 100}}
    ]
