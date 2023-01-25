
{{ config(
    alias="int_user_attributes"
    ,materialized="table"
) }}


SELECT
  md.user_id,
  md.person_id,
  md.core_marital_status,
  md.core_number_of_persons_in_living_unit,
  md.core_age,
  md.core_presence_of_children,
  md.core_homeowner,
  md.core_merkle_adjusted_wealth_rating,
  md.core_length_of_residence,
  md.family_id,
  md.address_id,
  md.core_household_income,
  md.core_probable_using_internet_for_general_entertainment,
  u.has_had_cancel,
  u.has_had_trial,
  u.times_cancelled,
  u.most_recent_subscription_start
FROM {{ ref('stg_merkle__datasources') }} as md
JOIN {{ source('ott','dim_user') }} as u
ON md.user_id = u.user_id
