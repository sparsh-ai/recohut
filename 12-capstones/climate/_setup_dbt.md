# DBT
Create a free dbt cloud account using this link https://www.getdbt.com/signup/
Note that the name and last name are used to create a dataset in BigQuery for development. E.g Marcos Jimenez -> mjimenez
Create a dbt cloud project:
Detailed instructions can be found here: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_4_analytics_engineering/dbt_cloud_setup.md#create-a-dbt-cloud-project

## 1. Create a project

- Main menu -> Account -> Projects -> New Project
  - Name: ghcn-d
  - Advanced settings: Project subdirectory: dbt
  - BigQuery
  - Upload a Service Account JSON file: Use the credentials file generated when setting up GPC account
  - Test
  - Continue
  - Git Clone -> Git URL: git@github.com:YOUR_GIT_USERNAME/ghcn-d.git
  - Import
  - Copy the generated deployment key
  - Go to your git provider (e.g. github) and edit the configuration of the project ghcn-d:  
    - Settings (Settings tab in the GitHub repository page)
    - Deploy keys
    - Add deploy keys
      - Name dbt
      - Paste the key
      - Allow write access
      - Add key
  - Continue
  - Skip & Complete

## 2. Create a production environment

    - Click Main Menu icon -> Environments
    - New Environment
    - Name: production
    - Type: deployment
    - Under deployment credentials, set Dataset: production
    - Save
  Note: If you do not see the Deployment credentials detail. Reload the page.
  
## 3. Create a job

  Create a job named 'dbt build' and set the following command with the specific range of years: 
  - Main menu
  - Jobs
  - New job
  - Name: dbt build
  - Environment: production
  - Commands:  `dbt run --vars "{'is_test_run': false,'start_year':2000,'end_year':2022}"`  
  - Disable run on schedule
  Note: Start_year and end_year defines the range of years to be processed. Be coherent with previous setup.  
  Note: Schedule will be either orchestrate through airflow or manually triggered.
  - Save
  
## 4. Create dbt api key file
If you want airflow to orchestrate dbt job, you will need an api key. API is available during free trial and for team and enterprise plans. If not, then no need to do this step. You will trigger manually the job in dbt.
  - Go to profile (upper-right icon)
  - Api access menu
  - Copy the api key
  - Create a txt file (i.e. apy_key.txt) containing the key and save it the VM under ~/.dbt (you can do it with VSCode)








