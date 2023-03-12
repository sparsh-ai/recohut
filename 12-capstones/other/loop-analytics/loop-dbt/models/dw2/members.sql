with max_delivery_pickup_dates as (
    select 
        loop_customer_id,
        min(delivery_date) as first_delivery_date,
        max(delivery_date) as most_recent_delivery_date,
        min(pick_up_date) as first_pick_up_date,
        max(pick_up_date) as most_recent_pick_up_date
    from {{ref('loops')}} 
    group by loop_customer_id
),

count_loops as (
    select loop_customer_id,
        sum(case when delivery_date <= sysdate and (pick_up_date is null or pick_up_date >= sysdate) then 1 else 0 end) as number_items_in_home,
        sum(case when delivery_date > sysdate and (pick_up_date is null or pick_up_date >= sysdate) then 1 else 0 end) as number_items_delivery_scheduled,
        sum(case when pick_up_date > sysdate then 1 else 0 end) as number_items_scheduled_pickup,
        max(case when sku in ('7116326076587', '413', '6650335723691', '7282008326315', '410') then 1 else 0 end) as snoo_customer,
        min(case when sku in ('7116326076587', '413', '6650335723691', '7282008326315', '410') then 1 else 0 end) as snoo_only_customer,
        count(distinct sku) as distinct_item_loops,
        count(*) as count_total_loops
    from {{ref('loops')}} 
    group by 1
), 

membership_subscriptions_stripe as (
    select sh.id as subscription_id,
        cim.loop_customer_id,
        sh.current_period_end,
        sh.current_period_start,
        sh.created,
        sh.canceled_at,
        sh.cancel_at,
        sh.ended_at,
        sh.status,
        prod.name as product_name,
        row_number() over(partition by sh.customer_id order by sh.created) as rn
    from {{source('stripe_fivetran', 'subscription_history')}} sh inner join
        {{source('stripe_fivetran', 'subscription_item')}} si on sh.id = si.subscription_id inner join
        {{source('stripe_fivetran', 'price')}} p on si.plan_id = p.id inner join
        {{source('stripe_fivetran', 'product')}} prod on p.product_id = prod.id left join
        {{ref('customer_id_map')}} cim on sh.customer_id = cim.stripe_customer_id
    where sh._fivetran_active = true and 
        (prod.name ilike '%monthly%' or prod.name ilike '%annual%') and
        sh.created > '2022-08-01'
), 

membership_subscriptions_bold as (
    select s.id as subscription_id,
        coalesce(cim.loop_customer_id, bc.platform_id) as loop_customer_id,
        s.next_order_datetime as current_period_end,
        s.last_order_datetime as current_period_start,
        s.created_at as created,
        s.status_changed_at,
        s.subscription_status as status,
        p.product_name,
        row_number() over(partition by s.customer_id order by s.created_at) as rn
    from {{source('bold', 'subscriptions')}} s inner join
        {{source('bold', 'line_items')}} li on s.id = li.subscription_id inner join
        {{source('bold', 'customers')}} bc on s.customer_id = bc.id left join
        {{source('shopify', 'customers')}} sc on bc.platform_id = sc.id left join
        {{ref('customer_id_map')}} cim on sc.id = cim.shopify_customer_id left join 
        {{ref('products')}} p on li.platform_product_id = p.sku
    where p.product_name ilike '%monthly%' or p.product_name ilike '%annual%'
), 

membership_subscriptions as (
    select s.subscription_id,
        s.loop_customer_id,
        s.current_period_end,
        s.current_period_start,
        coalesce(b.created, s.created) as created,
        s.canceled_at,
        s.cancel_at,
        s.ended_at,
        s.status,
        s.product_name,
        case when b.loop_customer_id is not null then 'bold and stripe' else 'stripe' end as src
    from membership_subscriptions_stripe s left join
        membership_subscriptions_bold b on s.loop_customer_id = b.loop_customer_id and s.rn = 1 and b.rn = 1

    union all

    select b.subscription_id,
        b.loop_customer_id,
        b.current_period_end,
        b.current_period_start,
        b.created,
        case when b.status = 'inactive' then status_changed_at else null end as canceled_at,
        null as cancel_at,
        case when b.status = 'inactive' then status_changed_at else null end as ended_at,
        b.status,
        b.product_name,
        'bold' as src
    from membership_subscriptions_bold b left join
        membership_subscriptions_stripe s on s.loop_customer_id = b.loop_customer_id and s.rn = 1 and b.rn = 1
    where s.loop_customer_id is null
),

max_payment_dates as (
    select loop_customer_id,
        min(created_at) as first_order_date,
        max(created_at) as last_order_date
    from {{ref('payments')}} 
    where transacation_type != 'refund'
    group by 1
),

shopify_service_area as (
    select coalesce(cim.loop_customer_id, json_extract_path_text(customer, 'id')) as loop_customer_id,
        json_extract_path_text(o.shipping_address, 'province') as province,
        row_number() over (partition by coalesce(cim.loop_customer_id, json_extract_path_text(customer, 'id')) order by o.created_at) as rn
    from {{source('shopify', 'orders')}} o left join
        {{ref('customer_id_map')}} cim on json_extract_path_text(customer, 'id') = cim.shopify_customer_id
    where json_extract_path_text(o.shipping_address, 'province') != ''
),

bigcommerce_service_area as (
    select cim.loop_customer_id,
        sa.state,
        row_number() over (partition by cim.loop_customer_id order by o.date_created) as rn
    from {{source('bigcommerce', 'shipping_addresses')}} sa left join
        {{source('bigcommerce', 'orders')}} o on sa.order_id = o.id left join
        {{ref('customer_id_map')}} cim on o.customer_id = cim.bigcommerce_customer_id
    where sa.state is not null
),

preactive_bigcommerce_membership_type as (
    select cim.loop_customer_id,
        li.name,
        row_number() over(partition by o.customer_id order by o.date_created) as rn
    from {{source('bigcommerce', 'line_items')}} li left join
        {{source('bigcommerce', 'orders')}} o on li.order_id = o.id left join
        {{ref('customer_id_map')}} cim on o.customer_id = cim.bigcommerce_customer_id left join
        {{source('dw2', 'account')}} a on cim.loop_customer_id = a.loopcustomerid
    where li.name ilike '%membership%' and 
        a.customertype = 'pre-active' and 
        o.status_id >= 2
)

select 
    a.loopcustomerid as loop_customer_id,
    a.emailaddress as email,
    coalesce(bcc.first_name, shc.first_name) as first_name,
    coalesce(bcc.last_name, shc.last_name) as last_name,
    case when a.membershipperiod != '' or a.customertype = 'pre-active' then 'Member'
        when me.exception_type in ('Registry', 'Used Goods', 'Gifter') then 'Non-Member Customer'
        when me.exception_type in ('Ottobie', 'Per Item', 'Influencer', 'Partner') then 'Member' 
        when ms.status in ('inactive', 'canceled') then 'Previous Member'
        else 'None' end as customer_type,
    case when (me.exception_type = 'Employee' or a.customertype = 'loop_employee') and a.membershipperiod != '' then 'Other Member'
        when me.exception_type in ('Influencer', 'Partner') then 'Other Member'
        when a.membershipperiod = 'year' and datediff(day, ms.canceled_at::date, ms.created::date) < 60 then 'Monthly'
        when a.membershipperiod = 'year' then 'Annual' 
        when a.membershipperiod = 'month' then 'Monthly' 
        when a.customertype = 'pre-active' and pbmt.name ilike '%month%' then 'Monthly'
        when a.customertype = 'pre-active' and pbmt.name ilike '%annual%' then 'Annual'
        when me.exception_type in ('Ottobie', 'Per Item') then 'Other Member'
        when me.exception_type = 'Registry' then 'Registry Purchased'
        when me.exception_type = 'Gifter' then 'Gifter'
        when me.exception_type = 'Used Goods' then 'Used Goods'
        when me.exception_type = 'Shopify Registrant' then 'Registrant'
        when a.customertype = 'Prospect' then 'Lead'
        when ms.status in ('inactive', 'canceled') then 'Previous Member'
        else 'None' end as customer_sub_type,
    case when coalesce(stc.address_state, bcsa.state, ssa.province, me.service_area, hc.state) in ('New York', 'New Jersey', 'Connecticut', 'NY', 'NJ', 'CT', 'NYC') then 'NYC'
        when coalesce(stc.address_state, bcsa.state, ssa.province, me.service_area, hc.state) in ('California', 'CA', 'SF') then 'SF'
        else 'Other' end as service_area,
    case when me.membership_status in ('Active', 'Free of Charge', 'Influencer') then 'Active'
        when me.membership_status = 'Churned' then 'Churned'
        when me.membership_status = 'Not Active' then 'Inactive'
        when (cl.number_items_in_home is null and a.membershipstatus = 'active') or (ms.canceled_at <= sysdate and a.membershipstatus = 'active') then 'Inactive'
        when a.customertype = 'pre-active' then 'Pre-Active'
        when a.customertype = 'active' then 'Active'
        when ms.status in ('inactive', 'canceled') then 'Churned'
        else a.membershipstatus end as membership_status,
    case when me.membership_status = 'Active' then 'Active'
        when me.membership_status = 'Churned' then 'Churned'
        when me.membership_status = 'Not Active' then 'Inactive'
        when me.membership_status in ('Free of Charge', 'Influencer', 'Employee') then 'Free of Charge'
        when (cl.number_items_in_home is null and a.membershipstatus = 'active') then 'At Risk'
        when (ms.canceled_at <= sysdate and a.membershipstatus = 'active') then 'Pre-Churn'
        when ms.status in ('inactive', 'canceled') then 'Churned'
        when a.customertype = 'pre-active' then 'Pre-Active'
        when a.customertype = 'active' then 'Active'
        else a.membershipstatus end as membership_sub_status,
    case when a.membershipperiod != '' or a.customertype = 'pre-active' or me.exception_type in ('Ottobie', 'Per Item', 'Influencer', 'Partner') then true 
        else false end as current_member_flag,
    cl.number_items_in_home,
    cl.number_items_delivery_scheduled,
    cl.number_items_scheduled_pickup,
    cl.count_total_loops,
    cl.distinct_item_loops,
    case when cl.snoo_only_customer = 1 then 'SNOO Only' 
        when cl.snoo_customer = 1 and cl.snoo_only_customer = 0 then 'SNOO and other products'
        when a.membershipstatus = 'none' then null
        else 'No SNOO' end as snoo_customer,
    case when me.exception_type = 'Registry' then null 
        when me.member_start_date is not null then me.member_start_date 
        when mdpd.first_delivery_date is not null and a.loopcustomerdate is not null then greatest(mdpd.first_delivery_date, a.loopcustomerdate::date) 
        else coalesce(mdpd.first_delivery_date, a.loopcustomerdate::date) end as member_start_date,
    mdpd.first_delivery_date,
    mdpd.most_recent_delivery_date,
    a.loopaccountcreated as account_created_date,
    mpd.first_order_date,
    mpd.last_order_date,
    mdpd.most_recent_pick_up_date,
    ms.current_period_end as next_renewal_date,
    ms.current_period_start as last_membership_payment_date,
    ms.canceled_at as cancellation_date,
    case when me.member_end_date is not null then member_end_date 
        when ms.status in ('inactive', 'canceled') then coalesce(ms.ended_at, ms.cancel_at) 
        else null end as churn_date,
    hc.reason_for_canceling,
    hc.child_1_dob,
    hc.child_2_dob,
    hc.child_3_dob,
    least(hc.child_1_dob, child_2_dob, child_3_dob) as youngest_child_dob,
    case when hc.child_1_dob is not null and hc.child_2_dob is not null and child_3_dob is not null then '3 or more'
        when child_1_dob is null and child_2_dob is null and child_3_dob is null then '0 or unknown'
        else (case when child_1_dob is not null then 1 else 0 end + 
            case when child_2_dob is not null then 1 else 0 end + 
            case when child_3_dob is not null then 1 else 0 end)::text 
        end as number_of_children,
    hc.expecting_at_sign_up,
    case when a.platform = 'bold' then 'Shopify' 
        when a.platform = 'stripe' then 'Stripe/BigCommerce' end as platform
from {{source('dw2','account')}} a left join
    {{source('bigcommerce', 'customers')}} bcc on a.bigcommercecustomerid = bcc.id left join
    {{source('shopify', 'customers')}} shc on a.shopifycustomerid = shc.id left join
    {{source('stripe_fivetran', 'customer')}} stc on a.stripecustomerid = stc.id left join
    {{source('hubspot', 'contacts')}} hc on a.hubspotcustomerid = hc.id left join
    max_delivery_pickup_dates mdpd on a.loopcustomerid = mdpd.loop_customer_id left join
    {{ref('_member_exceptions')}} me on a.emailaddress = me.email left join 
    count_loops cl on a.loopcustomerid = cl.loop_customer_id left join
    membership_subscriptions ms on a.loopcustomerid = ms.loop_customer_id left join
    max_payment_dates mpd on a.loopcustomerid = mpd.loop_customer_id left join
    bigcommerce_service_area bcsa on a.loopcustomerid = bcsa.loop_customer_id and bcsa.rn = 1 left join
    shopify_service_area ssa on a.loopcustomerid = ssa.loop_customer_id and ssa.rn = 1 left join
    preactive_bigcommerce_membership_type pbmt on a.loopcustomerid = pbmt.loop_customer_id and pbmt.rn = 1

--membership exceptions
union 
select 
    coalesce(me.email, me.shopify_id) as loop_customer_id,
    me.email,
    null as first_name,
    null as last_name,
    case when me.exception_type in ('Registry', 'Used Goods', 'Gifter') then 'Non-Member Customer'
        when me.exception_type in ('Ottobie', 'Per Item', 'Influencer', 'Partner') then 'Member' 
        else 'None' end as customer_type,
    case when me.exception_type in ('Employee', 'Influencer', 'Partner') then 'Other Member'
        when me.exception_type in ('Ottobie', 'Per Item') then 'Other Member'
        when me.exception_type = 'Registry' then 'Registry Purchased'
        when me.exception_type = 'Gifter' then 'Gifter'
        when me.exception_type = 'Used Goods' then 'Used Goods'
        when me.exception_type = 'Shopify Registrant' then 'Registrant'
        else 'None' end as customer_sub_type,
    me.service_area,
    case when me.membership_status in ('Active', 'Free of Charge', 'Influencer') then 'Active'
        when me.membership_status = 'Churned' then 'Churned'
        when me.membership_status = 'Not Active' then 'Inactive' 
        else null end as membership_status,
    case when me.membership_status = 'Active' then 'Active'
        when me.membership_status = 'Churned' then 'Churned'
        when me.membership_status = 'Not Active' then 'Inactive'
        when me.membership_status in ('Free of Charge', 'Influencer', 'Employee') then 'Free of Charge'
        else null end as member_sub_status,
    case when me.exception_type in ('Ottobie', 'Per Item', 'Influencer', 'Partner') then true
        else false end as current_member_flag,
    null as number_items_in_home,
    null as number_items_delivery_scheduled,
    null as number_items_scheduled_pickup,
    null as count_total_loops,
    null as distinct_item_loops,
    null as snoo_customer,
    null as member_start_date,
    null as first_delivery_date,
    null as most_recent_delivery_date,
    null as account_created_date,
    null as first_order_date,
    null as last_order_date,
    null as most_recent_pick_up_date,
    null as next_renewal_date,
    null as last_membership_payment_date,
    null as cancellation_date,
    null as churn_date,
    null as reason_for_canceling,
    null as child_1_dob,
    null as child_2_dob,
    null as child_3_dob,
    null as youngest_child_dob,
    null as number_of_children,
    null as expecting_at_sign_up,
    case when me.exception_type = 'Ottobie' then 'Ottobie'
        when me.exception_type in ('Registry', 'Gifter', 'Per Item') then 'Shopify'
        else 'Stripe/BigCommerce' end as platform
from {{ref('_member_exceptions')}} me left join
    {{source('dw2', 'account')}} a on me.email = a.emailaddress
where a.loopcustomerid is null

