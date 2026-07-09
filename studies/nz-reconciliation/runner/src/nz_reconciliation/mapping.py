"""OpenFisca Aotearoa mapping status for NZ reconciliation cases."""

from __future__ import annotations

from typing import Any

# Verified against ServiceInnovationLab/openfisca-aotearoa checkout (2026-07-09):
# - parameters/taxes/income_tax/individual_income_tax_rate.yaml exists (rates/thresholds
#   last updated 2010-10-01; no 2026 brackets).
# - variables/acts/income_tax/individual.py computes taxable_income from gross/deductions
#   but has no progressive tax-liability formula over those brackets.
# - variables/acts/acc/* covers LOPE/weekly compensation eligibility, not earners levy.
# - No KiwiSaver contribution variables or parameters found.
OPENFISCA_ENGINE_GAPS: dict[str, dict[str, str]] = {
    "income_tax": {
        "status": "engine_gap",
        "classification": "engine_gap",
        "notes": (
            "openfisca-aotearoa exposes income_tax__taxable_income and a 2010-vintage "
            "individual_income_tax_rate parameter tree, but no variable computes "
            "progressive income tax before credits for a taxable-income input. "
            "Cannot reconcile RuleSpec individual_income_tax_before_credits."
        ),
        "evidence": (
            "openfisca_aotearoa/variables/acts/income_tax/individual.py; "
            "openfisca_aotearoa/parameters/taxes/income_tax/individual_income_tax_rate.yaml"
        ),
    },
    "acc_earners_levy": {
        "status": "engine_gap",
        "classification": "engine_gap",
        "notes": (
            "openfisca-aotearoa ACC modules model LOPE/weekly compensation eligibility "
            "(acc_sched_1__*, acc__earner, etc.), not ACC earners levy rates, caps, or "
            "standard/self-employed levy amounts."
        ),
        "evidence": "openfisca_aotearoa/variables/acts/acc/",
    },
    "kiwisaver": {
        "status": "engine_gap",
        "classification": "engine_gap",
        "notes": (
            "No KiwiSaver contribution variables, parameters, or tests found in "
            "openfisca-aotearoa. RuleSpec KiwiSaver compile is also blocked upstream "
            "(TheAxiomFoundation/rulespec-nz#79)."
        ),
        "evidence": "repo-wide search for kiwisaver (no matches under openfisca_aotearoa/)",
    },
}


def openfisca_mapping_for_case(case: dict[str, Any]) -> dict[str, str]:
    """Return OpenFisca mapping metadata for one inventory case."""
    domain = str(case.get("domain") or "")
    gap = OPENFISCA_ENGINE_GAPS.get(domain)
    if gap is None:
        return {
            "status": "pending_mapping",
            "classification": "unclassified",
            "notes": f"No OpenFisca mapping policy for domain={domain!r}",
            "evidence": "",
        }
    return dict(gap)


def annotate_inventory_case(case: dict[str, Any]) -> dict[str, Any]:
    """Return a shallow-copied case with openfiscaAotearoa mapping filled in."""
    annotated = dict(case)
    mapping = openfisca_mapping_for_case(case)
    existing = dict(case.get("openfiscaAotearoa") or {})
    existing.update(
        {
            "status": mapping["status"],
            "notes": mapping["notes"],
            "classification": mapping["classification"],
            "evidence": mapping["evidence"],
        }
    )
    annotated["openfiscaAotearoa"] = existing
    return annotated
