# SNAP Divergence Source-Level Classification

This classification is over the 15 held candidate divergences. It is source-level classified, but not a legal adjudication of which engine is correct.

## Summary

- Divergences classified: 15
- Remaining unclassified divergences: 0

## Counts

| Classification | Count |
|---|---:|
| deduction handling | 4 |
| parameter vintage | 3 |
| state-option modeling | 8 |

## Cases

| Case | Classification | Decision-relevant | Detail |
|---|---|---|---|
| `us-snap/fixture.ga_bbce_165_boundary` | state-option modeling | true | Georgia limited-BBCE divergence: PRD snapData carries BBCE_State=Yes but a 1.30 gross-FPL threshold, while PolicyEngine routes the state option through TANF non-cash categorical eligibility with a 1.30 gross threshold and no TANF non-cash net/asset constraint. Legal correctness is not adjudicated here. |
| `us-snap/fixture.ga_gross_130_above` | state-option modeling | true | Georgia limited-BBCE divergence: PRD snapData carries BBCE_State=Yes but a 1.30 gross-FPL threshold, while PolicyEngine routes the state option through TANF non-cash categorical eligibility with a 1.30 gross threshold and no TANF non-cash net/asset constraint. Legal correctness is not adjudicated here. |
| `us-snap/fixture.ga_gross_130_below` | state-option modeling | true | Georgia limited-BBCE divergence: PRD snapData carries BBCE_State=Yes but a 1.30 gross-FPL threshold, while PolicyEngine routes the state option through TANF non-cash categorical eligibility with a 1.30 gross threshold and no TANF non-cash net/asset constraint. Legal correctness is not adjudicated here. |
| `us-snap/fixture.ms_asset_above_limit` | state-option modeling | true | Asset-test divergence: PRD applies direct SNAP asset-test columns to totalassets in function.snapBenefit, while PolicyEngine routes BBCE through TANF non-cash eligibility and state asset-limit parameters before SNAP categorical eligibility. Legal correctness is not adjudicated here. |
| `us-snap/fixture.ms_bbce_165_boundary` | parameter vintage | true | Mississippi non-BBCE divergence: PRD snapData has BBCE_State=No, GrossIncomeEligibilityFPL=1.30, finite AssetTest_nonelddis=3000, and non-waived net tests; PolicyEngine represents non-BBCE TANF non-cash eligibility with negative-infinity gross/asset parameters while normal SNAP eligibility uses federal SNAP tests. The result is source-level classified as a parameter-surface/vintage mismatch pending legal adjudication. |
| `us-snap/fixture.ms_gross_130_above` | parameter vintage | true | Mississippi non-BBCE divergence: PRD snapData has BBCE_State=No, GrossIncomeEligibilityFPL=1.30, finite AssetTest_nonelddis=3000, and non-waived net tests; PolicyEngine represents non-BBCE TANF non-cash eligibility with negative-infinity gross/asset parameters while normal SNAP eligibility uses federal SNAP tests. The result is source-level classified as a parameter-surface/vintage mismatch pending legal adjudication. |
| `us-snap/fixture.ms_gross_130_below` | parameter vintage | true | Mississippi non-BBCE divergence: PRD snapData has BBCE_State=No, GrossIncomeEligibilityFPL=1.30, finite AssetTest_nonelddis=3000, and non-waived net tests; PolicyEngine represents non-BBCE TANF non-cash eligibility with negative-infinity gross/asset parameters while normal SNAP eligibility uses federal SNAP tests. The result is source-level classified as a parameter-surface/vintage mismatch pending legal adjudication. |
| `us-snap/fixture.ms_utility_allowance_phone_only` | deduction handling | false | Mississippi phone-only utility divergence: PRD applies the SNAP utility deduction through HCSUA/HCSUAValue when utilities are positive and rounds annual snapValue; PolicyEngine chooses between SUA/LUA/IUA from distinct utility bills and uses the Mississippi phone allowance parameter. The remaining difference is non-decision-relevant. |
| `us-snap/fixture.pa_bbce_165_boundary` | deduction handling | true | Pennsylvania Heat-and-Eat/SUA divergence: PRD's snapData has HeatandEatState=Yes and HCSUAValue=778.466, with utility deduction triggered inside function.snapBenefit; PolicyEngine marks PA as always-SUA and uses its utility-allowance parameter table. The observed offset is a deduction/parameter-surface mismatch, not an eligibility flip. |
| `us-snap/fixture.pa_gross_130_above` | deduction handling | true | Pennsylvania Heat-and-Eat/SUA divergence: PRD's snapData has HeatandEatState=Yes and HCSUAValue=778.466, with utility deduction triggered inside function.snapBenefit; PolicyEngine marks PA as always-SUA and uses its utility-allowance parameter table. The observed offset is a deduction/parameter-surface mismatch, not an eligibility flip. |
| `us-snap/fixture.pa_gross_130_below` | deduction handling | true | Pennsylvania Heat-and-Eat/SUA divergence: PRD's snapData has HeatandEatState=Yes and HCSUAValue=778.466, with utility deduction triggered inside function.snapBenefit; PolicyEngine marks PA as always-SUA and uses its utility-allowance parameter table. The observed offset is a deduction/parameter-surface mismatch, not an eligibility flip. |
| `us-snap/fixture.tx_asset_above_limit` | state-option modeling | true | Asset-test divergence: PRD applies direct SNAP asset-test columns to totalassets in function.snapBenefit, while PolicyEngine routes BBCE through TANF non-cash eligibility and state asset-limit parameters before SNAP categorical eligibility. Legal correctness is not adjudicated here. |
| `us-snap/fixture.tx_bbce_165_boundary` | state-option modeling | true | Texas BBCE divergence: PRD encodes BBCE_State=Yes, GrossIncomeEligibilityFPL=1.65, and AssetTest_nonelddis=5000 in snapData and then applies direct gross/asset gates; PolicyEngine encodes the same state-option surface through TANF non-cash gross, net, and asset tests feeding SNAP categorical eligibility. Legal correctness is not adjudicated here. |
| `us-snap/fixture.tx_gross_130_above` | state-option modeling | true | Texas BBCE divergence: PRD encodes BBCE_State=Yes, GrossIncomeEligibilityFPL=1.65, and AssetTest_nonelddis=5000 in snapData and then applies direct gross/asset gates; PolicyEngine encodes the same state-option surface through TANF non-cash gross, net, and asset tests feeding SNAP categorical eligibility. Legal correctness is not adjudicated here. |
| `us-snap/fixture.tx_gross_130_below` | state-option modeling | true | Texas BBCE divergence: PRD encodes BBCE_State=Yes, GrossIncomeEligibilityFPL=1.65, and AssetTest_nonelddis=5000 in snapData and then applies direct gross/asset gates; PolicyEngine encodes the same state-option surface through TANF non-cash gross, net, and asset tests feeding SNAP categorical eligibility. Legal correctness is not adjudicated here. |

## Source Evidence

### `us-snap/fixture.ga_bbce_165_boundary`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/meets_snap_categorical_eligibility.py#L12-L17
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/is_tanf_non_cash_eligible.py#L11-L15
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_net_income_test.py#L11-L24
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117

### `us-snap/fixture.ga_gross_130_above`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/meets_snap_categorical_eligibility.py#L12-L17
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/is_tanf_non_cash_eligible.py#L11-L15
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_net_income_test.py#L11-L24
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117

### `us-snap/fixture.ga_gross_130_below`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/meets_snap_categorical_eligibility.py#L12-L17
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/is_tanf_non_cash_eligible.py#L11-L15
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_net_income_test.py#L11-L24
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117

### `us-snap/fixture.ms_asset_above_limit`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/meets_snap_categorical_eligibility.py#L12-L17
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/is_tanf_non_cash_eligible.py#L11-L15
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_asset_test.py#L11-L29
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/asset_limit.yaml#L32-L103

### `us-snap/fixture.ms_bbce_165_boundary`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_asset_test.py#L11-L29
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/asset_limit.yaml#L32-L103

### `us-snap/fixture.ms_gross_130_above`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_asset_test.py#L11-L29
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/asset_limit.yaml#L32-L103

### `us-snap/fixture.ms_gross_130_below`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_asset_test.py#L11-L29
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/asset_limit.yaml#L32-L103

### `us-snap/fixture.ms_utility_allowance_phone_only`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/income/deductions/shelter/snap_utility_allowance_type.py#L20-L39
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/usda/snap/income/deductions/utility/always_standard.yaml#L23-L94
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/usda/snap/income/deductions/utility/single/phone.yaml#L358-L368
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/snap_expected_contribution.py#L13-L19

### `us-snap/fixture.pa_bbce_165_boundary`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/income/deductions/shelter/snap_utility_allowance_type.py#L20-L39
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/usda/snap/income/deductions/utility/always_standard.yaml#L23-L94

### `us-snap/fixture.pa_gross_130_above`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/income/deductions/shelter/snap_utility_allowance_type.py#L20-L39
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/usda/snap/income/deductions/utility/always_standard.yaml#L23-L94

### `us-snap/fixture.pa_gross_130_below`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/income/deductions/shelter/snap_utility_allowance_type.py#L20-L39
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/usda/snap/income/deductions/utility/always_standard.yaml#L23-L94

### `us-snap/fixture.tx_asset_above_limit`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/meets_snap_categorical_eligibility.py#L12-L17
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/is_tanf_non_cash_eligible.py#L11-L15
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_asset_test.py#L11-L29
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/asset_limit.yaml#L32-L103

### `us-snap/fixture.tx_bbce_165_boundary`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/meets_snap_categorical_eligibility.py#L12-L17
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/is_tanf_non_cash_eligible.py#L11-L15
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_net_income_test.py#L11-L24
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_asset_test.py#L11-L29
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/asset_limit.yaml#L32-L103

### `us-snap/fixture.tx_gross_130_above`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/meets_snap_categorical_eligibility.py#L12-L17
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/is_tanf_non_cash_eligible.py#L11-L15
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_net_income_test.py#L11-L24
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_asset_test.py#L11-L29
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/asset_limit.yaml#L32-L103

### `us-snap/fixture.tx_gross_130_below`

- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708
- https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/meets_snap_categorical_eligibility.py#L12-L17
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/is_tanf_non_cash_eligible.py#L11-L15
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_net_income_test.py#L11-L24
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_asset_test.py#L11-L29
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117
- https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/asset_limit.yaml#L32-L103

