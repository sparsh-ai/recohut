-- This is a stupid query to satisfy some UI needs
select
    date
    , 'total' as member_type
    , '1. new' as member_status
    , current_new_members
from {{ ref('kpis_by_day') }}

union all

select
    date
    , 'total' as member_type
    , '2. scheduled' as member_status
    , current_scheduled_members
from {{ ref('kpis_by_day') }}

union all

select
    date
    , 'total' as member_type
    , '3. active' as member_status
    , current_active_members
from {{ ref('kpis_by_day') }}

union all

select
    date
    , 'total' as member_type
    , '4. inactive' as member_status
    , current_inactive_members
from {{ ref('kpis_by_day') }}

{% for mtype in ['annual', 'monthly', 'per_item'] %}
union all

select
    date
    , '{{ mtype }}' as member_type
    , '1. new' as member_status
    , current_new_{{ mtype }}_members
from {{ ref('kpis_by_day') }}

union all

select
    date
    , '{{ mtype }}' as member_type
    , '2. scheduled' as member_status
    , current_scheduled_{{ mtype }}_members
from {{ ref('kpis_by_day') }}

union all

select
    date
    , '{{ mtype }}' as member_type
    , '3. active' as member_status
    , current_active_{{ mtype }}_members
from {{ ref('kpis_by_day') }}

union all

select
    date
    , '{{ mtype }}' as member_type
    , '4. inactive' as member_status
    , current_inactive_{{ mtype }}_members as member_count
from {{ ref('kpis_by_day') }}
{% endfor %}
