# ITEM_SPECIFICATION_COMPONENT_BR

Last Edited: 29/03/2023

## Description

This object is the atomic level bridge table for packaging. Containing both Evolve Food and Valpak, this performs all the cleaning and calculations that need to take place prior to being consumed in the PL layer. This object supports FACT_ITEM_SPECIFICATION_COMPONENT and AGG_ITEM_PRIMARY_PLASTICS.

## Source to Target

These tables are assumed to be unioned in the spec and will have the name OP, AP and VALPAK as aliases:

* ADW_PRODUCT_TRAN.ITEM_PACKAGING_COMPONENT_VALPAK_HIST_BR_LOGIC_2 as VALPAK
* ADW_RDV.ADVANCED_PACKAGING_COMPONENT_LINK as AP
* ADW_RDV.ITEM_SPECIFICATION_ITEM_PACKAGING_COMPONENT_LINK as OP

| **Source Tables**| **Source Columns**| **Target Column**         |
|------------------|-------------------|---------------------------|
| AVG_WEIGHT_HIST_BR_01  VALPAK <br>_BR | ITEM_NK1 <br> ITEM_CD | ITEM_CD|
| VALPAK <br> AP,OP | SPECIFICATION_VERSION_SK_CD CONCAT(ITEM_SPEC_NK1,ITEM_SPEC_NK2) |SPECIFICATION_VERSION_CD|
| VALPAK <br> AP, OP | PACKAGING_VALPAK_SK_CD <br> ITEM_PACKAGING_CD | PACKAGING_CD |
| VALPAK <br> AP, OP | COMPONENT_VALPAK_SK_CD <br> ITEM_PACKAGING_COMPONENT_CD | COMPONENT_CD |
| VALPAK <br>ITEM_SPECIFICATION_SUPPLIER_SITE_LINK | ALPHANUMERIC_SUPPLIER_CD <br> ITEM_SUPPLIER_CD | ALPHANUMERIC_SUPPLIER_CD  |
| VALPAK <br>AP, OP | RECYCLING_ADVICE_CD <br> RECYCLING_ADVICE_ICON | RECYCLING_ADVICE_CD |
| AGG_FINANCE_PNL_METRIC | SALES_INITIATED_LOCATION_CD | COUNTRY |
| AGG_FINANCE_PNL_METRIC | TRAN_DT                     | FIN_PERIOD_NUM |
| VALPAK <br> AP, OP | AVERAGE_PACKAGING_COMPONENT_WEIGHT<br>COMPONENT_WEIGHT_GRAMS | COMPONENT_WEIGHT |
| VALPAK <br> AP, OP | AVERAGE_PACKAGING_RECYCLED_WEIGHT<br>RECYCLED_GRAMS | COMPONENT_RECYCLED_WEIGHT |
| VALPAK <br> AP, OP | RECYCLED_WEIGHT_PCT<br>RECYCLED_GRAMS | RECYCLED_WEIGHT_PCT       |
| AGG_FINANCE_PNL_METRIC | SALES_VOLUME   | SALES_VOLUME              |
| N/A                    | N/A   CALCULATED FIELD | TOTAL_TONNAGE             |
| N/A                    | N/A   CALCULATED FIELD | RECYCLED_TONNAGE          |
| VALPAK <br> AP,   OP   |                        | SOURCE_SYSTEM_CD          |
| N/A                    | N/A                    | LOAD_TS                   |
| N/A                    | N/A                    | TECHNICAL_METADATA        |

## Mapping steps, rules and calculations

Calculations

* Secondary weight calculation:
    * COMPONENT_WEIGHT / CASE_CRATE_SHIPPER_QTY
Example :
Case component weight = 352.59 g
Case crate shipper quantity = 12
Secondary Calculated weight = 352.59/12 = 29.3 g
* Tertiary weight calculation:
    * COMPONENT_WEIGHT / (CASE_CRATE_SHIPPER_QTY * TOTAL_CASES_PER_PALLET_LAYER_QTY)
Example :
Stretch Wrap component weight = 250
Case crate shipper quantity = 12
Case crate total cases per pallet = 42
Tertiary Calculated weight = 250/(12*42) = 0.49603 g
* Multipack calculation:
    * CONSUMER_PACK_QTY * COMPONENT_WEIGHT
Example :
Component weight from Evolve for bottle = 34 gm
Calculated Weight for Bottle = 4 * 34 gm = 136 gm
* Recycled weight calculation:
    * Calculated Recycled Content Weight =% Recycled Content * Calculated Component Weight
* Multiple component supplier calculation:
    * A spefication and version has multiple suppliers of a component, for example in our data we will have three entries against a bottle, however only one bottle will have sold in the store. Therefore we have to take this into consideration when building both fact views. For packaging we have worked out the average value of the three components, then divided by the no. of components to give an accurate figure when rolling up to the views consumed by the business:
        * Example:
            * Bottle 32g,Bottle 36g, Bottle 33g
            * Average value = 33.6 g / 3 = 11.2 g

Rules

* An Item has more than one supplier. This is an issue because the finance data doesn't include supplier info, so how do we proportion the units correctly. There is a method devised to take the stock holdings of the supplier and apply a weighted percentage of the units to each supplier.

Mapping Steps

1) Filter both Valpak and Evolve sources with the supporting SQL given to ensure correct data and no duplication into the final table.
1) Combine original packaging, advanced packaging, supplier site & evolve sat for packaging data.
1) Apply above calculations on packaging data.
1) Aggregate sales volume by fin period num.
1) Add in country data to sales volume.
1) Apply stock and sales rule.
1) Combine sales data with packaging data.
1) Apply tonnage calculations with sales and packaging data.
1) Load TS to table.
1) End.

## Supporting SQL
***
```sql
-- This identifies the business units and sub categories applicable to Valpak

SELECT 
SUB_CAT_CD,
SUB_CAT_NAME,
BUSINESS_UNIT_CD,
BUSINESS_UNIT_NAME,
OWN_LABEL_FLAG
FROM 
ADW_PROD.ADW_PRODUCT_TRAN.ITEM_PACKAGING_COMPONENT_VALPAK_HIST_BR_LOGIC_2 V
INNER JOIN 
ADW_PRODUCT_PL.DIM_ITEM DIM ON DIM.ITEM_CD = V.ITEM_CD
WHERE 
OWN_LABEL_FLAG = 'Y'
AND
CASE WHEN
BUSINESS_UNIT_CD 
IN (5699,3210)
THEN  
SUB_CAT_CD IN 
(
184,319,325,350,353,438,468,502,503,533,607,654,849,850,856,876,877,880,881,882,883,884,886,887,888,889,891,892,893,894,895,896,912,913,929,943
)
ELSE SUB_CAT_CD END
GROUP BY 1,2,3,4,5
ORDER BY 3,1;

-- This identifies the business units and sub categories applicable to Evolve
SELECT 
SUB_CAT_CD,
SUB_CAT_NAME,
BUSINESS_UNIT_CD,
BUSINESS_UNIT_NAME,
OWN_LABEL_FLAG
FROM ADW_PROD.ADW_PRODUCT_TRAN.ITEM_SPECIFICATION_COMPONENT_BR_LOGIC_1 E
INNER JOIN ADW_PRODUCT_PL.DIM_ITEM DIM ON DIM.ITEM_CD = E.ITEM_NK1
WHERE OWN_LABEL_FLAG = 'Y'
AND
BUSINESS_UNIT_CD IN (5699,3210)
AND
SUB_CAT_CD NOT IN 
(
184,319,325,350,353,438,468,502,503,533,607,654,849,850,856,876,877,880,881882,883,884,886,887,888,889,891,892,893,894,895,896,912,913,929,943
)
GROUP BY 1,2,3,4,5
ORDER BY 2;
```

## Diagram

![Alt text](ITEM%20SPECIFICATION%20COMPONENT%20BR.png)

## Tests & Checks

- [ ] Secondary & Tertiary calculations applied
- [ ] Multipack calculations applied
- [ ] Supplier weighting applied
- [ ] Sales volume is the same in br table as source
- [ ] Tonnage and recycled tonnage calculations are verified