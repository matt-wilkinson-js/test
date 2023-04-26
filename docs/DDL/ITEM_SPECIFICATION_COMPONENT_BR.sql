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