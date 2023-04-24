# Homepage

## About
Data architecture mapping specifications for data product dp-c3fn-packaging

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## **Mapping specs**
#### Stage
### RDV
### BDV
[ITEM_SPECIFICATION_COMPONENT_BR](http://127.0.0.1:8000/mapping_spec_example/)
### PL

## DDL'S
#### ITEM_SPECIFICATION_COMPONENT_BR
```sql
CREATE OR REPLACE TABLE ADW_BDV.ITEM_SPECIFICATION_COMPONENT_BR
(
 ITEM_CD                   number(38,0) NOT NULL COMMENT 'ITEM code',
 SPECIFICATION_VERSION_CD  varchar NOT NULL COMMENT 'Spec & Version',
 PACKAGING_CD              varchar NOT NULL COMMENT 'Packaging code.',
 COMPONENT_CD              varchar NOT NULL, COMMENT 'Component code',
 ALPHANUMERIC_SUPPLIER_CD  varchar NOT NULL COMMENT 'Alphanumeric Supplier Code',
 ENTERPRISE_SUPPLIER_CD    varchar NOT NULL, COMMENT 'Enterprise Code',
 RECYCLING_ADVICE_ICON     varchar NOT NULL COMMENT 'Recycling Advice',
 COUNTRY                   varchar NOT NULL COMMENT 'Country',
 TRAN_DT                   date NOT NULL COMMENT 'Sales transaction date.',
 FULFILMENT_CHANNEL_CD     number(38,0) NOT NULL COMMENT 'The channel of the sale e.g. in store',
 COMPONENT_WEIGHT          number(38,2) COMMENT 'Weight of each component.',
 COMPONENT_RECYCLED_WEIGHT number(38,2) COMMENT 'Weight of recycled content in the component.',
 RECYCLED_WEIGHT_PCT       number(38,2) COMMENT 'Recycled weight percentage',
 SALES_VOLUME              number(38,0) COMMENT 'Unit sales by item divided by the no of components in each spec & version.',
 TOTAL_TONNAGE             number(38,2) COMMENT 'Calculation to show plastic tonnage output.',
 RECYCLED_TONNAGE          number(38,2) COMMENT 'Calculation for recycled tonnage.',
 TECHNICAL_METADATA        variant NOT NULL COMMENT 'A JSON message of support fields. See Aspire modelling standards. Can be any of these: BATCH_ID
RECORD_ARRIVAL_TS
ETL_FRAMEWORK
HASH_DIFF
JOB_NAME
LOAD_TS
REASON_CD
RECORD_DELETED_FLAG
SOURCE_PATH
SOURCE_SYSTEM_CD
RECORD_ID
VALID_FROM_TS
VALID_TO_TS',

 CONSTRAINT ITEM_SPECIFICATION_COMPONENT_BR PRIMARY KEY ( ITEM_CD, SPECIFICATION_VERSION_CD, PACKAGING_CD, COMPONENT_CD, ALPHANUMERIC_SUPPLIER_CD, ENTERPRISE_SUPPLIER_CD, RECYCLING_ADVICE_ICON, COUNTRY, TRAN_DT, FULFILMENT_CHANNEL_CD )
)
COMMENT = 'This table combines Valpak & Evolve packaging data with sales to calculate the plastic and other material output in tonnes.';
```
#### AGG_ITEM_PRIMARY_PLASTICS
``` sql
CREATE OR REPLACE VIEW ADW_PRODUCT_PL.AGG_ITEM_PRIMARY_PLASTICS
(
 ITEM_CD              COMMENT 'ITEM code',
 GROUP_SUPPLIER_CD    COMMENT 'Group Supplier Code',
 RECYCLING_ADVICE_CD  COMMENT 'Recycling Advice',
 COUNTRY              COMMENT 'Country',
 CALNDR_PERIOD_NUM    COMMENT 'Calendar month.',
 ITEM_WEIGHT          COMMENT 'Weight of the items components.',
 ITEM_RECYCLED_WEIGHT COMMENT 'Weight of recycled content in the item.',
 RECYCLED_WEIGHT_PCT  COMMENT 'Percentage of the recycled content.',
 SALES_VOLUME         COMMENT 'Sales units.',
 TOTAL_TONNAGE        COMMENT 'Calculation to show plastic tonnage output.',
 RECYCLED_TONNAGE     COMMENT 'Calculation for recycled tonnage.',
 RECYCLABILITY_PCT    COMMENT 'Calculation for showing how much of the item can be recycled in future.'
)
COMMENT = 'An aggregated table based off ITEM_SPECIFICATION_COMPONENT_BR to fit the requirements of the Plan for Better Commercial dashboard.';
```
#### FACT_ITEM_SPECIFICATION_COMPONENT
``` sql
CREATE OR REPLACE VIEW ADW_PRODUCT_PL.FACT_ITEM_SPECIFICATION_COMPONENT
(
 ITEM_CD                   COMMENT 'ITEM code',
 SPECIFICATION_VERSION_CD  COMMENT 'Spec & Version',
 PACKAGING_COMPONENT_CD    COMMENT 'Packaging Code.',
 ENTERPRISE_SUPPLIER_CD    COMMENT 'Alphanumeric Supplier Code',
 RECYCLING_ADVICE_CD       COMMENT 'Recycling Advice',
 COUNTRY                   COMMENT 'Country',
 CALNDR_PERIOD_NUM         COMMENT 'Sales transaction month.',
 FULFILMENT_CHANNEL_CD     COMMENT 'Channel of the sale e.g. in store',
 COMPONENT_WEIGHT          COMMENT 'Weight of each component.',
 COMPONENT_RECYCLED_WEIGHT COMMENT 'Weight of recycled content in the component.',
 RECYCLED_WEIGHT_PCT       COMMENT 'Recycled weight percentage',
 SALES_VOLUME              COMMENT 'Unit sales by item divided by the no of components in each spec & version.',
 TOTAL_TONNAGE             COMMENT 'Calculation to show plastic tonnage output.',
 RECYCLED_TONNAGE          COMMENT 'Calculation for recycled tonnage.',
)
COMMENT = 'This table combines Valpak & Evolve packaging data with sales to calculate the plastic and other material output in tonnes.';
```
## Packaging Diagrams
### Dimensional Model
### Stage to PL Flow

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
