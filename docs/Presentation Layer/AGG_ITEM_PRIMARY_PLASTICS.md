# AGG_ITEM_PRIMARY_PLASTICS

**Last Edited: 27/04/2022**

## Description

This object is an aggregated fact view for the P4B Commercial dashboard. Containing Item level data, this view intends to analyse primary plastic packaging. The view is set to financial period for Sainsbury reporting requirements.

## Jira Tickets

| Jira Ticket | Description | Function |
|-------------|-------------|----------|
|[PFBP_381](https://sainsburys-jira.valiantys.net/browse/PFBP-381)| Analysis for adding in fulfilment channel and calendar reporting | Architecture

## Selection Criteria

This object is built from ITEM_SPECIFICATION_COMPONENT_BR, that tables time granulairty is date. For this view financial month is required, lookup TRAN_DT against DIM_DATE.DATE_DT and return FIN_PERIOD_NUM.

This object also needs to be filtered down to only include Primary Plastics.
```
* Concatenate the below primary keys in ITEM_SPECIFICATION_COMPONENT_BR:  
    * ITEM_CD
    * SPECIFICATION_VERSION_CD
    * PACKAGING_CD
    * COMPONENT_CD  
* Join to DIM_PACKAGING_COMPONENT using this key
* Filter PACKAGING_COMPONENT_LEVEL_CD = Primary
* Filter PACKAGING_COMPONENT_BASE_MATERIAL_DESC = Plastic
```

## Target to Source

{{ read_excel('Mapping Spec Git.xlsx', engine='openpyxl', sheet_name="AGG_ITEM_PRIMARY_PLASTICS") }} 

## Mapping Steps

1. Apply necessary selection criteria on ITEM_SPECIFICATION_COMPONENT_BR
1. Create a CTE containing financial periods as per selection criteria
1. Join the CTE to ITEM_SPECIFICATION_COMPONENT_BR using TRAN_DT and DATE_DT
1. Create groupings and sums
1. End

## Diagram

Not required for this build

## Tests & Checks 

[x] Object is filtered to Primary plastic
[x] Object is aggregated to financial periods
[x] Sales volume and weights deaggregate to source numbers