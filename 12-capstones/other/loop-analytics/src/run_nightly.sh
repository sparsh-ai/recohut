#/usr/bin/bash

set -e 

cd ..

source venv/bin/activate

echo "extracting hubspot"
python sync_hubspot.py

echo "extracting shopify"
python sync_shopify.py

echo "extracting bigcommerce"
python sync_bigcommerce.py

echo "extracting dynamo"
python sync_dynamo.py

echo "updating quickbase"
python sync_quickbase.py --qb_table_name products --schema_name dw --dw_table_name products_vw --to_quickbase
python sync_quickbase.py --qb_table_name customers --schema_name dw --dw_table_name customers --to_quickbase
python sync_quickbase.py --qb_table_name addresses --schema_name dw --dw_table_name shipping_addresses --to_quickbase
python sync_quickbase.py --qb_table_name orders --schema_name dw --dw_table_name non_subscription_orders --to_quickbase
python sync_quickbase.py --qb_table_name order_lines --schema_name dw --dw_table_name non_subscription_line_items --to_quickbase

echo "extracting bold"
python sync_bold.py

echo "extract ip locations"
python sync_ip_locations.py

echo "sync quickbase to redshift"
python sync_quickbase.py -dw

echo "extracting google sheets"
# python sync_google_sheets.py  -wb "Loop Inventory Management" -tb "inventory_reporting_base" -up
python sync_google_sheets.py  -wb "NEW - Loop Master" -sh "Loop Master" -tb "loop_master" -up
python sync_google_sheets.py  -wb "NEW - Loop Master" -sh "Purchase Master" -tb "purchase_master" -up
python sync_google_sheets.py  -wb "Loop Daily Targets - Integer Method" -sh "NEW_FINAL" -tb "loop_daily_targets" -up
python sync_google_sheets.py  -wb "Loop - Marketing Dashboard" -sh "FB Ad Key" -tb "fb_ad_key" -up
python sync_google_sheets.py  -wb "NYC - Loop Master" -sh "Loop Master" -tb "nyc_loop_master" -up
python sync_google_sheets.py  -wb "NYC - Loop Master" -sh "Purchase Master" -tb "nyc_purchase_master" -up

echo "loading tables to google sheets"
python sync_google_sheets.py  -wb "LoopDataWarehouseTables" -sh "dim_member" -sc "dw" -tb "dim_members" -dn -o contact_created_ts member_id -wc "WHERE membership_start_dt <= CURRENT_DATE"
python sync_google_sheets.py  -wb "LoopDataWarehouseTables" -sh "dim_item" -sc "dw" -tb "dim_item" -dn -o purchase_date sku
python sync_google_sheets.py  -wb "LoopDataWarehouseTables" -sh "dim_product" -sc "dw" -tb "dim_product" -dn -o product_created_ts sku
python sync_google_sheets.py  -wb "Loop Promotion Analytics - Copy" -sh "member_sales_agg" -sc "dw_aggs" -tb "member_sales_agg" -dn

deactivate
