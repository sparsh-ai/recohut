{% macro select_stats_overview(alias, date_agg, cluster_by='') -%}

    {{-
        config(
            alias=alias,
            cluster_by=cluster_by,
            unique_key='timestamp'
        )
    -}}

    WITH
        overall AS (
            SELECT
                  {{ date_agg }} AS timestamp
                , COUNT(DISTINCT session_id) AS count_active_sessions
                , COUNT(DISTINCT user_id) AS count_active_users
                , COUNT(DISTINCT client_id) AS count_active_clients
            FROM {{ ref('logs') }}
            GROUP BY timestamp
        )
        , pageviews AS (
            SELECT
                  {{ date_agg }} AS timestamp
                , COUNT(*) AS _count
            FROM {{ ref('pageviews')}}
            GROUP BY timestamp
        )
        , pa AS (
            SELECT
                  {{ date_agg }} AS timestamp
                , product_action
                , COUNT(*) AS _count
                , COUNT(DISTINCT session_id, product_id) AS count_distinct_session_products
                , COUNT(DISTINCT product_id) AS count_distinct_product_ids
                , SUM(product_quantity) AS sum_product_quantity
            FROM {{ ref('product_actions')}}
            GROUP BY timestamp, product_action
        )
        , purchases AS (
            SELECT
                  {{ date_agg }} AS timestamp
                , COUNT(DISTINCT transaction_id) AS _count
                , SUM(transaction_revenue) AS sum_revenue
                , SUM(transaction_tax) AS sum_tax
                , SUM(transaction_shipping) AS sum_shipping
            FROM {{ ref('purchases')}}
            GROUP BY timestamp
        )
        , sessions AS (
            SELECT timestamp, COUNT(DISTINCT session_id) AS count_new_sessions
            FROM (
                SELECT {{ date_agg }} AS timestamp, session_id
                FROM {{ ref('logs') }}
                WHERE session_id IS NOT NULL
                QUALIFY ROW_NUMBER() OVER (
                    PARTITION BY TO_DATE(request_timestamp), session_id
                    ORDER BY request_timestamp
                ) = 1
            )
            GROUP BY timestamp
        )
        , users AS (
            SELECT timestamp, COUNT(DISTINCT user_id) AS count_new_users
            FROM (
                SELECT {{ date_agg }} AS timestamp, user_id
                FROM {{ ref('logs') }}
                WHERE user_id IS NOT NULL
                QUALIFY ROW_NUMBER() OVER (
                    PARTITION BY TO_DATE(request_timestamp), user_id
                    ORDER BY request_timestamp
                ) = 1
            )
            GROUP BY timestamp
        )
        , clients AS (
            SELECT timestamp, COUNT(DISTINCT client_id) AS count_new_clients
            FROM (
                SELECT {{ date_agg }} AS timestamp, client_id
                FROM {{ ref('logs') }}
                WHERE client_id IS NOT NULL
                QUALIFY ROW_NUMBER() OVER (
                    PARTITION BY TO_DATE(request_timestamp), client_id
                    ORDER BY request_timestamp
                ) = 1
            )
            GROUP BY timestamp
        )


    SELECT
          o.timestamp

        , IFNULL(o.count_active_sessions, 0) AS count_active_sessions
        , IFNULL(sessions.count_new_sessions, 0) AS count_new_sessions

        , IFNULL(o.count_active_users, 0) AS count_active_users
        , IFNULL(users.count_new_users, 0) AS count_new_users

        , IFNULL(o.count_active_clients, 0) AS count_active_clients
        , IFNULL(clients.count_new_clients, 0) AS count_new_clients

        , IFNULL(pageviews._count, 0) AS pageviews

        , IFNULL(pa_click._count, 0) AS sum_of_product_clicks
        , IFNULL(pa_click.count_distinct_session_products, 0) AS product_clicks

        , IFNULL(pa_detail._count, 0) AS sum_of_product_details
        , IFNULL(pa_detail.count_distinct_session_products, 0) AS product_details

        , IFNULL(pa_add._count, 0) AS sum_of_add_to_cart
        , IFNULL(pa_add.count_distinct_session_products, 0) AS add_to_cart

        , IFNULL(pa_remove._count, 0) AS sum_of_remove_from_cart
        , IFNULL(pa_remove.count_distinct_session_products, 0) AS remove_from_cart

        , IFNULL(purchases._count, 0) AS transactions
        , IFNULL(purchases.sum_revenue, 0.0) AS transaction_revenue
        , IFNULL(purchases.sum_tax, 0.0) AS transaction_tax
        , IFNULL(purchases.sum_shipping, 0.0) AS transaction_shipping

        , IFNULL(pa_purchase.sum_product_quantity, 0) AS purchased_items
        , IFNULL(pa_purchase.count_distinct_product_ids, 0) AS purchased_products

        , SYSDATE()::timestamp_ntz AS created_at

    FROM overall AS o

    LEFT JOIN sessions ON sessions.timestamp = o.timestamp
    LEFT JOIN users ON users.timestamp = o.timestamp
    LEFT JOIN clients ON clients.timestamp = o.timestamp
    LEFT JOIN pageviews ON pageviews.timestamp = o.timestamp
    LEFT JOIN purchases ON purchases.timestamp = o.timestamp

    LEFT JOIN pa AS pa_click ON
            pa_click.timestamp = o.timestamp
        AND pa_click.product_action = 'click'
    LEFT JOIN pa AS pa_add ON
            pa_add.timestamp = o.timestamp
        AND pa_add.product_action = 'add'
    LEFT JOIN pa AS pa_remove ON
            pa_remove.timestamp = o.timestamp
        AND pa_remove.product_action = 'remove'
    LEFT JOIN pa AS pa_detail ON
            pa_detail.timestamp = o.timestamp
        AND pa_detail.product_action = 'detail'
    LEFT JOIN pa AS pa_purchase ON
            pa_purchase.timestamp = o.timestamp
        AND pa_purchase.product_action = 'purchase'

    ORDER BY timestamp DESC

{%- endmacro %}
