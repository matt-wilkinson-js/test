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