# Loop Analytics

Extracing data and loading it to Redshift, and a dbt project for transforming it.

## Structure

### DBT

### (E)mpirical (R)oot ETL - ERetl

## Additional Notes

### Dealing with customers that have multiple accounts

*Consolidate the accounts under 1 member_id using* `dbt.data._duplicates.csv`

Under the loop-dbt/data/ directory exists a file called `_duplicates.csv` which is a hard coded table to identify customers who have more than one account. We use that to identify the preferred account by providing the preferred `member_id`

For each system where the customer has a duplicate record there should be an entry in the `_duplicates.csv` table. Choosing the shared/primary member_id of the preferred record.

The ephemeral table `ephemeral.member_id_map.sql` then uses that duplicates table to map users from any of the connected systems (e.g. hubspot, spotify, etc) to the *primary* `member_id`

All the other tables should be using the member_id_map to connect a customer to the primary `member_id`.

In the case that a system does not have access to one of the system's ids like the hubspot.contact_id, but does have access the the email, one can get the primary member_id by looking up the md5(lower(trim(*email*))) as the `email_key` in the `ephemeral.member_id_by_email` mapping. 

for example:
```
select 
    member_id_by_email.member_id
    , my_table.*
from 
    my_table
    left join {{ ref('member_id_by_email') }} as member_id_by_email 
        on md5(lower(trim(my_table.email_field_with_weird_name))) = member_id_by_email.email_key
```

## Solution

```
├── [1.0K]  config
│   └── [ 957]  config_example.yaml
├── [1.6K]  loop-analytics.md
├── [1.2M]  loop-dbt
│   ├── [ 14K]  analysis
│   │   ├── [2.0K]  LOOP-122_monthly_member_churn_agg.sql
│   │   ├── [3.1K]  annual_churn_category.sql
│   │   ├── [ 396]  email_capture_signups.sql
│   │   ├── [1.6K]  fact_loop_old.sql
│   │   ├── [1.8K]  pdp_prep_post_analysis.sql.ignore
│   │   ├── [ 757]  product_as_first_page_view.sql
│   │   ├── [3.4K]  q1_rebate.sql
│   │   └── [ 597]  snoo_duration.sql
│   ├── [588K]  data
│   │   ├── [ 211]  _bundled_products.csv
│   │   ├── [ 478]  _duplicate_emails.csv
│   │   ├── [3.3K]  _duplicates.csv
│   │   ├── [ 11K]  _line_item_sku_override.csv
│   │   ├── [ 329]  _manual_products.csv
│   │   ├── [8.4K]  _member_exceptions.csv
│   │   ├── [3.5K]  _member_overrides.csv
│   │   ├── [ 17K]  _transaction_sku_override.csv
│   │   ├── [1.1K]  dim_channel.csv
│   │   ├── [541K]  dim_date.csv.zip
│   │   ├── [  56]  points.csv
│   │   └── [1.6K]  seeds.yml
│   ├── [ 733]  dbt_project.yml
│   ├── [2.3K]  macros
│   │   ├── [ 404]  generate_schema_name.sql
│   │   ├── [1.5K]  hacks.sql
│   │   └── [ 244]  utils.sql
│   ├── [621K]  models
│   │   ├── [ 59K]  aggs
│   │   │   ├── [ 841]  abandoned_cart_mix.sql
│   │   │   ├── [2.8K]  agg_member_waterfall.sql
│   │   │   ├── [1.4K]  agg_registry.sql.ignore
│   │   │   ├── [  70]  bigcommerce_completed_orders.sql
│   │   │   ├── [5.8K]  channel_performance_daily.sql
│   │   │   ├── [1.4K]  checkout_view_loss.sql
│   │   │   ├── [2.5K]  cohort_base.sql
│   │   │   ├── [ 149]  discount_codes.sql
│   │   │   ├── [1.5K]  klayvio_customer_data.sql.ignore
│   │   │   ├── [ 16K]  kpis_by_day.sql
│   │   │   ├── [  36]  last_data_refresh.sql
│   │   │   ├── [ 718]  loop_daily_targets.sql
│   │   │   ├── [8.5K]  member_agg.sql.ignore
│   │   │   ├── [2.1K]  member_attribution_agg.sql.ignore
│   │   │   ├── [ 459]  member_sales_agg.sql
│   │   │   ├── [2.6K]  mrr_by_customer_month_transpose.sql
│   │   │   ├── [2.0K]  mrr_customer_reshape_henry.sql
│   │   │   ├── [1.2K]  new_customer_by_day.sql
│   │   │   ├── [2.1K]  order_attribution_base.sql.ignore
│   │   │   ├── [ 522]  product_page_views.sql
│   │   │   ├── [ 891]  product_view_loss_agg.sql
│   │   │   ├── [1.3K]  products_with_more_than_five_payments.sql
│   │   │   ├── [2.2K]  sku_agg.sql
│   │   │   └── [1.4K]  wide2long_member_histograms.sql
│   │   ├── [ 55K]  dw
│   │   │   ├── [4.9K]  combined
│   │   │   │   ├── [ 687]  fact_line_item.sql
│   │   │   │   ├── [1.1K]  fact_order.sql
│   │   │   │   ├── [ 472]  fact_refund.sql
│   │   │   │   ├── [ 653]  fact_refund_line_item.sql
│   │   │   │   ├── [ 716]  fact_transaction.sql
│   │   │   │   └── [1.1K]  sessioned_events_combined.sql
│   │   │   ├── [1.7K]  customer_ids.sql
│   │   │   ├── [1.3K]  dim_ad.sql
│   │   │   ├── [ 970]  dim_campaign.sql
│   │   │   ├── [2.0K]  dim_item.sql
│   │   │   ├── [ 32K]  dim_members.sql
│   │   │   ├── [ 501]  dim_membership.sql
│   │   │   ├── [1.9K]  dim_product.sql
│   │   │   ├── [ 421]  dim_subscriptions.sql
│   │   │   ├── [ 991]  fact_ad_performance.sql
│   │   │   ├── [ 863]  fact_daily_depreciation.sql
│   │   │   ├── [ 684]  fact_daily_revenue.sql
│   │   │   ├── [ 762]  fact_discounts.sql
│   │   │   ├── [2.8K]  fact_loop.sql
│   │   │   ├── [ 448]  fact_message_clicked.sql
│   │   │   ├── [ 427]  fact_message_delivered.sql
│   │   │   ├── [ 421]  fact_message_opened.sql
│   │   │   └── [1.2K]  order_ids_map.sql
│   │   ├── [ 69K]  dw2
│   │   │   ├── [ 830]  customer_id_map.sql
│   │   │   ├── [ 875]  deliveries.sql
│   │   │   ├── [ 760]  discounts.sql
│   │   │   ├── [1.3K]  inventory.sql
│   │   │   ├── [2.3K]  line_items.sql
│   │   │   ├── [ 745]  logistics.sql
│   │   │   ├── [2.7K]  loops.sql
│   │   │   ├── [ 298]  member_history.sql.ignore
│   │   │   ├── [ 15K]  members.sql
│   │   │   ├── [   0]  orders.sql
│   │   │   ├── [6.7K]  payments.sql
│   │   │   ├── [1.0K]  pickups.sql
│   │   │   ├── [2.3K]  products.sql
│   │   │   ├── [6.5K]  sessioned_events.sql
│   │   │   ├── [9.1K]  site_activity.sql
│   │   │   ├── [4.7K]  subscriptions.sql
│   │   │   └── [ 12K]  web_activity.sql
│   │   ├── [ 31K]  ephemeral
│   │   │   ├── [5.7K]  _member_type_inputs.sql
│   │   │   ├── [  95]  dates.sql
│   │   │   ├── [   0]  existing_subscription_to_charge.sql
│   │   │   ├── [ 333]  loopshare_discount_hack.sql
│   │   │   ├── [1.8K]  member_baskets_loop.sql
│   │   │   ├── [1.6K]  member_baskets_platform.sql
│   │   │   ├── [ 125]  member_id_by_email.sql
│   │   │   ├── [3.1K]  member_id_map.sql
│   │   │   ├── [  66]  member_initial_baskets_loop.sql
│   │   │   ├── [  70]  member_initial_baskets_platform.sql
│   │   │   ├── [  66]  member_second_baskets_loop.sql
│   │   │   ├── [  69]  member_second_baskets_platform.sql
│   │   │   ├── [ 499]  members_with_hacked_annual_membership.sql
│   │   │   ├── [1.9K]  membership_orders.sql
│   │   │   ├── [ 419]  non_refunded_line_items.sql
│   │   │   ├── [  80]  numbers.sql
│   │   │   ├── [ 426]  recurring_subscription_invoice.sql
│   │   │   ├── [ 13K]  shopify
│   │   │   │   ├── [5.8K]  _member_type_inputs_shopify.sql
│   │   │   │   ├── [1.8K]  member_baskets_loop_shopify.sql
│   │   │   │   ├── [1.6K]  member_baskets_shopify.sql
│   │   │   │   ├── [1.8K]  member_id_map_shopify.sql
│   │   │   │   ├── [  75]  member_initial_baskets_loop_shopify.sql
│   │   │   │   ├── [  70]  member_initial_baskets_shopify.sql
│   │   │   │   ├── [  75]  member_second_baskets_loop_shopify.sql
│   │   │   │   ├── [  70]  member_second_baskets_shopify.sql
│   │   │   │   ├── [ 514]  members_with_hacked_annual_membership_shopify.sql
│   │   │   │   └── [1.1K]  membership_orders_shopify.sql
│   │   │   └── [ 516]  sku_avg_price.sql
│   │   ├── [ 23K]  finance_reports
│   │   │   ├── [ 338]  bigcommerce_line_items.sql
│   │   │   ├── [ 174]  bigcommerce_orders.sql
│   │   │   ├── [ 14K]  bold_subscriptions.sql
│   │   │   ├── [  33]  customers_id_map.sql
│   │   │   ├── [ 315]  shopify_line_items.sql
│   │   │   ├── [ 258]  shopify_orders.sql
│   │   │   ├── [ 344]  stripe_charges.sql
│   │   │   ├── [1.6K]  stripe_invoice_line_items.sql
│   │   │   └── [6.0K]  stripe_subscriptions.sql
│   │   ├── [ 17K]  qb_views
│   │   │   ├── [1.2K]  customers.sql
│   │   │   ├── [ 627]  filtered_order_lines.sql
│   │   │   ├── [ 610]  non_subscription_line_items.sql
│   │   │   ├── [ 649]  non_subscription_orders.sql
│   │   │   ├── [1.3K]  products_vw.sql
│   │   │   ├── [5.2K]  replatform
│   │   │   │   ├── [1.2K]  customers_rp.sql
│   │   │   │   ├── [2.7K]  non_subscription_line_items_rp.sql
│   │   │   │   └── [1.2K]  non_subscription_orders_rp.sql
│   │   │   ├── [1.3K]  shipping_addresses.sql
│   │   │   └── [5.4K]  shopify
│   │   │       ├── [ 350]  customers_shopify.sql
│   │   │       ├── [2.1K]  non_subscription_line_items_shopify.sql
│   │   │       ├── [1.3K]  non_subscription_orders_shopify.sql
│   │   │       ├── [1005]  order_shipping_addresses.sql
│   │   │       └── [ 548]  shipping_addresses_shopify.sql
│   │   ├── [1.2K]  report_tables
│   │   │   └── [1.1K]  registry_buyer_recipients
│   │   ├── [ 86K]  shopify_archived
│   │   │   ├── [2.8K]  agg_member_waterfall_shopify.sql
│   │   │   ├── [2.5K]  cohort_base_shopify.sql
│   │   │   ├── [ 33K]  dim_members_shopify.sql
│   │   │   ├── [ 531]  dim_membership_shopify.sql
│   │   │   ├── [ 447]  dim_product_shopify.sql
│   │   │   ├── [ 259]  dim_subscriptions_shopify.sql
│   │   │   ├── [ 871]  fact_daily_depreciation_shopify.sql
│   │   │   ├── [ 700]  fact_daily_revenue_shopify.sql
│   │   │   ├── [3.2K]  fact_loop_shopify.sql
│   │   │   ├── [ 12K]  fact_web_activity_shopify.sql
│   │   │   ├── [1.5K]  klaviyo_customer_data_shopify.sql.ignore
│   │   │   ├── [ 16K]  kpis_by_day_shopify.sql
│   │   │   ├── [9.9K]  member_agg_shopify.sql
│   │   │   ├── [ 475]  member_sales_agg_shopify.sql
│   │   │   └── [1.2K]  new_customers_by_day_shopify.sql
│   │   ├── [271K]  single_platform
│   │   │   ├── [1.2K]  fact_line_item_rp.sql
│   │   │   ├── [ 913]  fact_line_item_shopify.sql
│   │   │   ├── [3.0K]  fact_order_rp.sql
│   │   │   ├── [2.2K]  fact_order_shopify.sql
│   │   │   ├── [1.2K]  fact_refund_line_item_shopify.sql
│   │   │   ├── [1.1K]  fact_refund_line_items_rp.sql
│   │   │   ├── [ 968]  fact_refund_rp.sql
│   │   │   ├── [1.6K]  fact_refund_shopify.sql
│   │   │   ├── [4.2K]  fact_transaction_rp.sql
│   │   │   ├── [3.9K]  fact_transaction_shopify.sql
│   │   │   └── [250K]  sessioned_events_shopify.sql
│   │   ├── [10.0K]  sources.yml
│   │   └── [ 237]  testing
│   │       ├── [  84]  member_daily_change.sql
│   │       └── [  25]  member_day_before.sql
│   ├── [  96]  snapshots
│   └── [  96]  tests
├── [1.9K]  requirements.txt
├── [104K]  schema
│   ├── [ 13K]  bigcommerce
│   │   ├── [ 372]  brands.yaml
│   │   ├── [ 674]  categories.yaml
│   │   ├── [ 708]  customers.yaml
│   │   ├── [1.4K]  line_items.yaml
│   │   ├── [3.0K]  orders.yaml
│   │   ├── [3.1K]  products.yaml
│   │   ├── [ 511]  refunds.yaml
│   │   ├── [ 494]  shipments.yaml
│   │   ├── [1.3K]  shipping_addresses.yaml
│   │   └── [ 940]  variants.yaml
│   ├── [5.2K]  bold
│   │   ├── [ 973]  addresses.yaml
│   │   ├── [ 369]  customers.yaml
│   │   ├── [ 260]  labels.yaml
│   │   ├── [1.2K]  line_items.yaml
│   │   ├── [ 444]  shipping_lines.yaml
│   │   ├── [ 351]  subscription_summaries.yaml
│   │   └── [1.4K]  subscriptions.yaml
│   ├── [ 12K]  dw
│   │   ├── [3.7K]  cohort_data.sql
│   │   ├── [2.0K]  dim_member.sql
│   │   ├── [5.3K]  kpis_by_day.sql
│   │   └── [ 486]  scheduled_item_stats.sql
│   ├── [2.3K]  dynamo
│   │   ├── [ 305]  accounts_dev.yaml
│   │   ├── [ 306]  accounts_prod.yaml
│   │   ├── [  65]  accounts_sequence_dev.yaml
│   │   ├── [  66]  accounts_sequence_prod.yaml
│   │   ├── [  89]  bold_subscription_notification_dev.yaml
│   │   ├── [  90]  bold_subscription_notification_prod.yaml
│   │   ├── [  64]  carts_dev.yaml
│   │   ├── [  66]  carts_prod.yaml
│   │   ├── [ 124]  customer_migration_messages_dev.yaml
│   │   ├── [ 125]  customer_migration_messages_prod.yaml
│   │   ├── [ 116]  customer_migrations_dev.yaml
│   │   ├── [ 117]  customer_migrations_prod.yaml
│   │   ├── [  68]  customers_dev.yaml
│   │   ├── [  69]  customers_prod.yaml
│   │   ├── [  69]  registries_dev.yaml
│   │   └── [  71]  registries_prod.yaml
│   ├── [7.9K]  googlesheets
│   │   ├── [ 164]  fb_ad_key.yaml
│   │   ├── [1.9K]  inventory_reporting_base.yaml
│   │   ├── [ 558]  loop_daily_targets.yaml
│   │   ├── [1.0K]  loop_master.yaml
│   │   ├── [1007]  nyc_loop_master.yaml
│   │   ├── [1.5K]  nyc_purchase_master.yaml
│   │   └── [1.6K]  purchase_master.yaml
│   ├── [ 15K]  hubspot
│   │   ├── [9.6K]  contacts.yaml
│   │   └── [5.5K]  deals.yaml
│   ├── [ 642]  ip_api
│   │   └── [ 546]  ip_location.yaml
│   ├── [ 39K]  quickbase
│   │   ├── [1.4K]  associate_asset_tag.yaml
│   │   ├── [1.3K]  associate_customer_address_to_order.yaml
│   │   ├── [1.2K]  associate_inventory_location.yaml
│   │   ├── [1.7K]  cancel_performed_delivery.yaml
│   │   ├── [2.0K]  cancel_performed_pickup.yaml
│   │   ├── [1.9K]  cancel_scheduled_pickup.yaml
│   │   ├── [1.1K]  create_regional_inventory_transfer.yaml
│   │   ├── [ 827]  customers.yaml
│   │   ├── [2.0K]  inventory.yaml
│   │   ├── [1.4K]  inventory_locations.yaml
│   │   ├── [2.5K]  order_lines.yaml
│   │   ├── [2.8K]  perform_delivery.yaml
│   │   ├── [ 937]  perform_local_inventory_transfer.yaml
│   │   ├── [2.4K]  perform_qa.yaml
│   │   ├── [2.0K]  pick_cancellation.yaml
│   │   ├── [3.1K]  pick_deliveries.yaml
│   │   ├── [ 795]  receive_asset.yaml
│   │   ├── [1.2K]  receive_inventory_transfer.yaml
│   │   ├── [2.0K]  schedule_delivery.yaml
│   │   ├── [2.6K]  schedule_pickup.yaml
│   │   ├── [1.8K]  scheduled_delivery_cancellation.yaml
│   │   ├── [ 686]  scrap_asset.yaml
│   │   └── [ 753]  sell_asset.yaml
│   ├── [ 966]  reviewsio
│   │   └── [ 870]  merchant_reviews.yaml
│   └── [7.6K]  shopify
│       ├── [1016]  customers.yaml
│       ├── [1.2K]  line_items.yaml
│       ├── [3.4K]  orders.yaml
│       ├── [ 732]  products.yaml
│       └── [1.1K]  variants.yaml
├── [ 790]  smartsheet_templates
│   ├── [ 327]  dw
│   │   ├── [ 130]  fact_line_items.sql
│   │   └── [  69]  fact_order.sql
│   └── [ 335]  shopify
│       ├── [ 137]  line_items.sql
│       └── [  70]  orders.sql
└── [152K]  src
    ├── [ 241]  config.py
    ├── [ 582]  cron_job.sh
    ├── [ 57K]  make_segment_master.py
    ├── [5.9K]  postgres_resource.py
    ├── [ 12K]  redshift_resource.py
    ├── [2.4K]  run_nightly.sh
    ├── [3.3K]  s3_resource.py
    ├── [4.6K]  schema.py
    ├── [8.3K]  sync_bigcommerce.py
    ├── [9.1K]  sync_bold.py
    ├── [3.2K]  sync_dynamo.py
    ├── [7.8K]  sync_google_sheets.py
    ├── [7.8K]  sync_hubspot.py
    ├── [4.2K]  sync_ip_locations.py
    ├── [9.7K]  sync_quickbase.py
    ├── [3.4K]  sync_reviewsio.py
    ├── [5.1K]  sync_shopify.py
    └── [6.9K]  sync_smart_sheet.py

 1.5M used in 37 directories, 270 files
```

## References

1. https://github.com/Loop-baby/loop-data