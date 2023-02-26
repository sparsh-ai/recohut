Run the following commands:  
- `cd dbt_local`  
- `docker-compose build` (to create the images) 

To run dbt cli commands use `docker-compose run`. For instance, to build the dbt project in the production environment:  
- `docker-compose run dbt-pg-ghcnd build --target prod --vars "{'is_test_run': false,'start_year':1770,'end_year':1780}"` 
  
Note: This is not needed but, just for reference...  
  To run dbt_local from scratch and create a new project, run the following command before `docker-compose up`:  
  ` docker-compose run dbt-pg-ghcnd-init`
  ... to create a new project under current directory. Project name and connection will be asked.
  From the docker-compose.yaml file, dbt-pg-ghcnd-init service is started (run means to run a command in a running service, but if it is not running, it is launched, and the command is init) from dbt-pg-ghcnd-init image, made from the Dockerfile, which has entry point dbt, so we are executing dbt init, which will ask for some parameters to create the project:  
    - Enter the name of the project: ghcnd  
    - Enter 1 to select postgres adapter  
  Project is created under `./ghcnd` directory and `./dbt/profiles.yml` is created  
  Edit `./dbt/profiles.yml` to setup postgres adaptor for the outputs (dev/prod)  
 
