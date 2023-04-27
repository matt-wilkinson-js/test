# FACT_ITEM_SPECIFICATION_COMPONENT

**Last Edited: 27/04/2022**

## Description

This object is the atomic level fact view for packaging. Containing component level data, this view intends to analyse all packaging types at all packaging levels. The view is set to calendar month to aid in EPR reporting.

## Jira Tickets

| Jira Ticket | Description | Function |
|-------------|-------------|----------|
|[PFBP_381](https://sainsburys-jira.valiantys.net/browse/PFBP-381)| Analysis for adding in fulfilment channel and calendar reporting | Architecture

## Selection Criteria

This object is built from ITEM_SPECIFICATION_COMPONENT_BR, that tables time granulairty is date. For this view calendar month is required, lookup TRAN_DT against DIM_DATE.DATE_DT and return CALNDR_PERIOD_NUM.

## Target to Source

{{ read_excel('Mapping Spec Git.xlsx', engine='openpyxl', sheet_name="FACT_ITEM_SPECIFICATION_COMPONE") }} 

## Mapping Steps

Not required for this build

## Diagram

Not required for this build

## Tests & Checks 

[x] Object is aggregated to calendar month
[x] Object metrics deaggregate to source table values