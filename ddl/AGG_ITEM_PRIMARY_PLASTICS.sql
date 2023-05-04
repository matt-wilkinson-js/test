CREATE OR REPLACE VIEW ADW_PRODUCT_PL.AGG_ITEM_PRIMARY_PLASTICS
(
 ITEM_CD              COMMENT 'ITEM code',
 GROUP_SUPPLIER_CD    COMMENT 'Group Supplier Code',
 RECYCLING_ADVICE_CD  COMMENT 'Recycling Advice',
 COUNTRY              COMMENT 'Country',
 FIN_PERIOD_NUM    COMMENT 'Calendar month.',
 ITEM_WEIGHT          COMMENT 'Weight of the items components.',
 ITEM_RECYCLED_WEIGHT COMMENT 'Weight of recycled content in the item.',
 RECYCLED_WEIGHT_PCT  COMMENT 'Percentage of the recycled content.',
 SALES_VOLUME         COMMENT 'Sales units.',
 TOTAL_TONNAGE        COMMENT 'Calculation to show plastic tonnage output.',
 RECYCLED_TONNAGE     COMMENT 'Calculation for recycled tonnage.',
)
COMMENT = 'An aggregated table based off ITEM_SPECIFICATION_COMPONENT_BR to fit the requirements of the Plan for Better Commercial dashboard.';