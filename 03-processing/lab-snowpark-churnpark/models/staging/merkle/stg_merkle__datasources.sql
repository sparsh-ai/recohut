{{ config(
    alias="stg_merkle_datasource"
) }}

select
    -- ids / integers
    user_id as user_id,
    core_number_of_persons_in_living_unit as core_number_of_persons_in_living_unit,
    core_age as core_age,
    core_length_of_residence as core_length_of_residence,
    finance_wealth_predictor_score as finance_wealth_predictor_score,
    core_merkle_adjusted_wealth_rating as core_merkle_adjusted_wealth_rating,
    core_probable_using_internet_for_general_entertainment as core_probable_using_internet_for_general_entertainment,

    -- strings
    personid as person_id,
    familyid as family_id,
    addressid as address_id,
    core_household_income as core_household_income,
    core_marital_status as core_marital_status ,   
    core_presence_of_children as core_presence_of_children,
    core_homeowner as core_homeowner

from {{ source('merkle','merkle_datasource') }}