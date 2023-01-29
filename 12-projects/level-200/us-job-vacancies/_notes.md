# Work around the world

Have you ever tried to look for a visa sponsor job vacancy? Or looking for a job overall nowadays is a little bit
overwhelming because of the number of different places you have to go to find a list of vacancies.

This project goals is to unify and provide a simple normalized and unified database of job vacancies from several data
sources (datasets for historical purposes and APIs to more up-to-date jobs). The final data schema is a star-schema 
model to ease querying through the jobs list, whereas the job listing is the fact and the company, skills and provider
are the dimensions of our data model.

## Data Sources

### US Jobs on Dice.com DAG

 - Id: `dice_com_jobs_dag`
 - Source Type: CSV Dataset
 - Data Source: https://data.world/promptcloud/us-jobs-on-dice-com
    - A dataset of 22.000 USA tech job posts crawled from the dice.com jobs site. 
    - It contains the job title, description, company and skills (tags). 

Basically this DAG takes care of parsing the CSV from a S3 Bucket and staging it on our Redshift cluster to then upsert the dimensions and facts data.
It runs only once as this dataset will not be updated anymore, it's for historical comparison purpose only.

### JobTechDev.se Historical Jobs DAG

 - Id: `jobtechdev_se_historical_jobs_dag`
 - Source Type: JSON Dataset
 - Data Source: https://jobtechdev.se/api/jobs/historical/
    - A historical dataset of nordic job vacancies with anonymized data. It has 4.4 million job posts starting from 2006 until 2017. 
    - Altought this is a very large dataset it only contains informations about the job title, description and company. No skills were provided.

Basically this DAG takes care of parsing the JSON from a S3 Bucket and staging it on our Redshift cluster. 
As this historical dataset may be updated we parse it yearly, starting from 2006 and ending in 2017.

### Landing Jobs API DAG

 - Id: `landing_jobs_api_dag`
 - Source Type: JSON API
 - Source: https://landing.jobs/api/v1
    - Landing.jobs is one of the most used jobs websites for jobs across the Europe (the majority of the jobs posts is from Europe). At this time they have around 420 jobs available to fetch from their API.
    - The Landing Jobs API is very straight forward, as it has a well structured data model the only thing that is missing in the job endpoint was the company name inside the job vacancy payload.
    - So, for this source we have the job title, description, salary, relocation flag, skills (tags). Missing only the company name.
    - Almost forgot to mention that the results are paginated. So we will limit the number of pages we'll download.
    
Basically this DAG takes care of fetching the API results within a range of pages available.
As this is a very dynamic source, this DAG runs everyday at midnight to fetch new jobs from Landing.jobs.

### GitHub Jobs API DAG

 - Id: `github_jobs_api_dag`
 - Source Type: JSON API
 - Source: https://jobs.github.com/api
    - The Github Jobs API is very simple, it was just get the page you want to fetch and appends a `.json` suffix, then it will returns only data formatted in JSON.
    - Altought GitHub is the largest developer community, this source is the one with less jobs to fetch. Around 280 jobs found in their API.
    - It provides the job title, description and company name. But there is no normalized data regarding the skills required in the job.
    
This DAG takes care of requesting the landing.jobs API and fetch a limited range of jobs. 
It is ran everyday at midnight so we have fresh jobs posting every day.

### Stackoverflow RSS Feed DAG

 - Id: `stackoverflow_jobs_rss_feed_dag`
 - Source Type: RSS Feed (XML)
 - Source: https://stackoverflow.com/jobs/feed
    - The Stackoverflow RSS feed is the one that has more jobs available to fetch (1000 jobs to be more precise).
    - It is also the most complete: has the job title, description, the company information and also the skills required in the job.

This DAG takes of requesting the Stackoverflow Jobs RSS Feed. This is a single page request, but it returns 1000 jobs per time.
So I configured to run this DAG daily too.

### Angel.co jobs DAG

 - Id: `angel_co_jobs_dag`
 - Source Type: HTML Crawling (selenium)

This DAG uses selenium to crawl the angel.co website and store all the HTML that contains job vacancies.

### Algolia Search Index Jobs DAG

 - Id: `algoliasearch_index_jobs_dag`
 - Source Type: Warehouse (Database)

This DAG takes care of fetching all inserted jobs within the `job_vacancies` table and index it on the instant search engine
called Algolia.

## Data Schema

The purpose of this project is to assemble a dataset to ease query for jobs of a determined set of skills or company.
For that we don't need normalized informations. Instead we adopted a star schema because of it's scalability in terms of
reading and querying. 

To simplify our job listing we'll have only a single fact table with the job vacancies and two other tables to aggregate
data on companies and tags.

## Data dictionary

### Companies

 - Table name: `companies`
 - Type: dimension table
 
| Column | Type | Description |
| ------ | ---- | ----------- |
| `id` | `VARCHAR(500) NOT NULL` | The id of the company (a slugified version of its name). |
| `name` | `VARCHAR(500)` | The name of the company |
| `remote_url` | `VARCHAR(500) DEFAULT NULL` | The url of the site of this company (if found on source) |

### Tags

 - Table name: `tags`
 - Type: dimension table
 
| Column | Type | Description |
| ------ | ---- | ----------- |
| `tag` | `VARCHAR(255) NOT NULL` | The tag found on the job |

### Job Vacancies

 - Table name: `job_vacancies`
 - Type: fact table
 
| Column | Type | Description |
| ------ | ---- | ----------- |
| `id` | `VARCHAR(255) NOT NULL` | The primary key of this table. Identifies the job vacancy |
| `provider_id` | `VARCHAR(255) NOT NULL` | The provider id means from which data sources it came from. Currently we have these sources: `jobtechdevse` (dataset), `dice_com` (dataset), `github_jobs` (api), `landing_jobs` (api), `stackoverflow_jobs` (api) |
| `remote_id_on_provider` | `VARCHAR(500)` | The identification of this job on the provider |
| `remote_url` | `VARCHAR(500)` | The URL for the job posting (if exists) |
| `location` | `VARCHAR(255)` | The location (city) of the job |
| `currency_code` | `VARCHAR(3) DEFAULT NULL` | The currency code of this job's salary |
| `company_id` | `VARCHAR(500)` | The company identification, mainly it`s a _slugified_ version of the company's name |
| `company_name` | `VARCHAR(500)` | The company name |
| `title` | `VARCHAR(1000)` | The title of the job post |
| `description` | `VARCHAR(65535)` | The description of the job post |
| `tags` | `VARCHAR(65535) DEFAULT NULL` | The tags are the skills required in this job. Separated by comma. |
| `salary` | `NUMERIC(18,2) DEFAULT NULL` | The salary base for the job role |
| `salary_max` | `NUMERIC(18,2) DEFAULT NULL` | The maximum salary that the company is willing to pay |
| `salary_frequency` | `VARCHAR(50) DEFAULT NULL` | The frequency of the salary. Usually `anually` (if has salary on the job post). |
| `has_relocation_package` | `INT4 DEFAULT NULL` | Indicates wether this job vacancy offers relocation package for the candidate. (this does not means visa sponsorship) |
| `expires_at` | `TIMESTAMP DEFAULT NULL` | When this job vacancy post will expire? |
| `published_at` | `TIMESTAMP` | The date this job was posted. |