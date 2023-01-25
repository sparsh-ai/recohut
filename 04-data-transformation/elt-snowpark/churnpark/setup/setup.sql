//Create event table for logging - Private Preview feature needs to be enabled as of Nov 2022
  
create event table DBT_DEMO_EVENTS;
alter account set event_table = DBT_DEMO_EVENTS;
