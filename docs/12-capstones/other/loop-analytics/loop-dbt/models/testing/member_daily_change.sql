select * from {{ref('members')}} 

minus

select * from {{ref('member_day_before')}}