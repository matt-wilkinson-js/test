# AGG_ITEM_PRIMARY_PLASTICS

**Last Edited: 10/05/2022**

## Description

This object is an aggregated fact view for the P4B Commercial dashboard. Containing Item level data, this view intends to analyse primary plastic packaging. The view is set to financial period for Sainsbury reporting requirements.

## Jira Tickets

| Jira Ticket | Description | Function |
|-------------|-------------|----------|
|[PFBP_321](https://sainsburys-jira.valiantys.net/browse/PFBP-321)| Original build|Architecture & Engineering
|[PFBP_381](https://sainsburys-jira.valiantys.net/browse/PFBP-381)| Analysis for adding in fulfilment channel and calendar reporting | Architecture
|[PFBP_398](https://sainsburys-jira.valiantys.net/browse/PFBP-398)| Adding in new tonnage calculation for loose items, fixing duplicate rows and recycled weight pct calculation| Engineering

## Selection Criteria

This object needs to be filtered down to only include Primary Plastics.

```
* Concatenate the below primary keys in ITEM_SPECIFICATION_COMPONENT_BR:  
    * ITEM_CD
    * SPECIFICATION_VERSION_CD
    * PACKAGING_CD
    * COMPONENT_CD  
* Join to DIM_PACKAGING_COMPONENT using PACKAGING_COMPONENT_CD
* Filter PACKAGING_COMPONENT_LEVEL = Primary
* Filter PACKAGING_COMPONENT_BASE_MATERIAL_DESC = Plastic
```

## Target to Source

{{ read_excel('Mapping Spec Git.xlsx', engine='openpyxl', sheet_name="AGG_ITEM_PRIMARY_PLASTICS") }} 

## Mapping Steps

1. Get Group Supplier from ADW_RDV.SUPPLIER_GROUP_SISUPG_REF join using ALPHANUMERIC_SUPPLIER_CD
1. Create a CTE that captures:
    ```
    ITEM_CD
    FIN_PERIOD_NUM
    GROUP_SUPPLIER_CD
    RECYCLING_ADVICE_CD
    COUNTRY
    SUM(SALES_VOLUME)
    ```
    This is to ensure that when we create our tonnage calculations, all the sales volume is being considered rather than an apportioned amount.
1. Create another CTE that captures:
    ```
    ITEM_CD
    FIN_PERIOD_NUM
    GROUP_SUPPLIER_CD
    COUNTRY
    SUM(COMPONENT_WEIGHT)
    SUM(COMPONENT_RECYCLED_WEIGHT)
    COMPONENT_RECYCLED_WEIGHT/COMPONENT_WEIGHT AS RECYCLED_WEIGHT_PCT
    ```
    This is going to capture all our primary plastics information.
1. Filter the CTE using the Selection criteria given.
1. Inner Join both tables using:
    ```
    ITEM_CD
    FIN_PERIOD_NUM
    GROUP_SUPPLIER_CD
    RECYCLING_ADVICE_CD
    COUNTRY
    ```
    This creates a table that will have the correct sales volume and weight metrics for applying our tonnage calculations.
1. Join to DIM_ITEM on ITEM_CD, this is to capture a new tonnage calculation which uses:
    1. WEIGHED_AT_CHECKOUT_FLAG
    1. CATCHWEIGHT_FLAG
1. Create total tonnage calculation:
    ```
    WHEN CATCHWEIGHT_FLAG = 'Y' OR WEIGHED_AT_CHECKOUT_FLAG = 'Y'
    THEN SALES_VOLUME/1000
    ELSE 
    SALES_VOLUME * ITEM_WEIGHT/1000000 
    ```
1. Sum recycled tonnage cirectly from the table
1. Apply recycled weight pct calculation
1. End

## Diagram

Not required for this build

## Tests & Checks 

Please evidence examples of the below.

Evidence provided by Govind Seenivasan

[Evidence Spreadsheet](https://jsainsbury.sharepoint.com/:x:/r/teams/P4B/_layouts/15/Doc.aspx?sourcedoc=%7Bcdf038d4-7a2e-42dd-90ec-08301b258623%7D&action=edit&activeCell=%27Step%204%20V2%27!F18&wdinitialsession=b2ad8817-e1b2-45a9-b60b-b24fb5ffbf0e&wdrldsc=2&wdrldc=1&wdrldr=AccessTokenExpiredWarning%2CRefreshingExpiredAccessT)

- [x] Unique row per primary key, ITEM_CD,GROUP_SUPPLIER_CD,RECYCLING_ADVICE_ICON,COUNTRY,FIN_PERIOD_NUM
- [x] Object is filtered to Primary plastic
- [x] Object has aligned Sales Volume to AGG_FINANCE_PNL_METRIC/ITEM_SPECIFICATION_COMPONENT_BR
- [x] Tonnage calculation is split as per case statement
- [x] Tonnage calculations are working as expected
- [x] Recycled weight percentage has been calculated as expected