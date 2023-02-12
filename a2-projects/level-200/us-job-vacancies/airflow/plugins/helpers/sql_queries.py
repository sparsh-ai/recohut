class SqlQueries:

    recreate_staging_dice_com_jobs_table = ("""
        DROP TABLE IF EXISTS staging_dice_com_jobs;
        CREATE TABLE staging_dice_com_jobs (
            country_code VARCHAR(500),
            date_added DATE SORTKEY,
            job_board VARCHAR(500),
            job_description VARCHAR(65535),
            job_title VARCHAR(500),
            job_type VARCHAR(200),
            location VARCHAR(500),
            organization VARCHAR(500),
            page_url VARCHAR(1000),
            phone_number VARCHAR(500),
            salary VARCHAR(100),
            sector VARCHAR(5000)
        ) DISTSTYLE EVEN;
    """)

    select_companies_from_dice_jobs_staging_table = ("""
        select distinct  
            REPLACE(TRIM(regexp_replace(translate(
                LOWER(organization),
                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
            ), '[^a-z0-9\-]+', ' ')),' ', '-') as id,
            organization as name,
            NULL as remote_url
        from 
            staging_dice_com_jobs
        where 1 not in (select id from companies);
    """)

    select_tags_from_dice_jobs_staging_table = ("""
        with NS AS (
          SELECT 1 as n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL 
          SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10 UNION ALL 
          SELECT 11 UNION ALL SELECT 12 UNION ALL SELECT 13 UNION ALL SELECT 14 UNION ALL SELECT 15 UNION ALL 
          SELECT 16 UNION ALL SELECT 17 UNION ALL SELECT 18 UNION ALL SELECT 19 UNION ALL SELECT 20 UNION ALL 
          SELECT 21 UNION ALL SELECT 22 UNION ALL SELECT 23 UNION ALL SELECT 24 UNION ALL SELECT 25 UNION ALL 
          SELECT 26 UNION ALL SELECT 27 UNION ALL SELECT 28 UNION ALL SELECT 29 UNION ALL SELECT 30 UNION ALL 
          SELECT 31 UNION ALL SELECT 32 UNION ALL SELECT 33 UNION ALL SELECT 34 UNION ALL SELECT 35 UNION ALL 
          SELECT 36 UNION ALL SELECT 37 UNION ALL SELECT 38 UNION ALL SELECT 39 UNION ALL SELECT 40 UNION ALL 
          SELECT 41 UNION ALL SELECT 42 UNION ALL SELECT 43 UNION ALL SELECT 44 UNION ALL SELECT 45 UNION ALL 
          SELECT 46 UNION ALL SELECT 47 UNION ALL SELECT 48 UNION ALL SELECT 49 UNION ALL SELECT 50 UNION ALL 
          SELECT 51 UNION ALL SELECT 52 UNION ALL SELECT 53 UNION ALL SELECT 54 UNION ALL SELECT 55 UNION ALL 
          SELECT 56 UNION ALL SELECT 57 UNION ALL SELECT 58 UNION ALL SELECT 59 UNION ALL SELECT 60
        )
        select distinct 
            trim(split_part(sector, ',', NS.n)) as "tag"
        from NS
        inner join staging_dice_com_jobs S ON NS.n <= REGEXP_COUNT(S.sector, ',') + 1
        where LEN("tag") <= 50 and "tag" not in (select "tag" from tags)
    """)

    select_job_vacancies_from_dice_jobs_staging_table = ("""
        select distinct  
            concat(row_number() over (partition by 1), concat('-', 'dice_com')) as id,
            'dice_com' as provider_id,
            page_url as remote_id_on_provider,
            page_url as remote_url,
            location as location,
            null as currency_code,
            REPLACE(TRIM(regexp_replace(translate(
                LOWER(organization),
                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
            ), '[^a-z0-9\-]+', ' ')),' ', '-') as company_id,
            organization as company_name,
            job_title as title,
            job_description as description,
            sector as tags,
            null as salary,
            null as salary_max,
            null as salary_frequency,
            0 as has_relocation_package,
            TO_TIMESTAMP(date_added, 'YYYY-MM-DD') as published_at
        from 
            staging_dice_com_jobs
        where page_url not in (select remote_id_on_provider from job_vacancies where provider_id = 'dice_com')
    """)

    recreate_staging_jobtechdev_jobs_table = ("""
        DROP TABLE IF EXISTS staging_jobtechdev_jobs;
        CREATE TABLE staging_jobtechdev_jobs (
            address VARCHAR(500) DEFAULT NULL,
            agency_name VARCHAR(500),
            number_of_acting_sites INT4,
            work_period VARCHAR(255),
            working_hours VARCHAR(255),
            working_hours_description VARCHAR(500),
            published_at DATE SORTKEY,
            website VARCHAR(500),
            community_code VARCHAR(500),
            company_number VARCHAR(500),
            job_description VARCHAR(65535),
            job_number VARCHAR(50),
            job_title VARCHAR(500),
            zipcode VARCHAR(8),
            city VARCHAR(255),
            expires_at DATE, 
            urgency_level_description VARCHAR(500),
            duration VARCHAR(255),
            job_code VARCHAR(100)
        ) DISTSTYLE EVEN;
    """)

    select_jobtechdev_companies_from_staging = ("""
        select distinct 
            REPLACE(TRIM(regexp_replace(translate(
                LOWER(agency_name),
                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
            ), '[^a-z0-9\-]+', ' ')),' ', '-') as id,
            agency_name AS name,
            null as remote_url
        from 
            staging_jobtechdev_jobs
        where
            id not in (select id from companies);
    """)

    select_jobtechdev_jobs_from_staging = ("""
        select distinct
            md5(
                coalesce(agency_name, 'agency') || coalesce(job_title, 'title') || 
                coalesce(job_description, 'job_desc') || published_at
            ) as id,
            'jobtechdevse' as provider_id,
            REPLACE(TRIM(regexp_replace(translate(
                LOWER(
                    CONCAT(
                        CONCAT(
                            agency_name, 
                            CONCAT(' ', job_title)
                        ),
                        CONCAT(' ', published_at)
                    )
                 ),
                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
            ), '[^a-z0-9\-]+', ' ')),' ', '-') as remote_id_on_provider,
            null as remote_url,
            city as location,
            null as currency_code,
            REPLACE(TRIM(regexp_replace(translate(
                LOWER(agency_name),
                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
            ), '[^a-z0-9\-]+', ' ')),' ', '-') as company_id,
            agency_name as company_name,
            job_title as title,
            job_description as description,
            null as tags,
            null as salary,
            null as salary_max,
            null as salary_frequency,
            0 as has_relocation_package,
            TO_TIMESTAMP(expires_at, 'YYYY-MM-DD') as expires_at,
            TO_TIMESTAMP(published_at, 'YYYY-MM-DD') as published_at
        FROM
            staging_jobtechdev_jobs
        WHERE id NOT IN (SELECT j.id FROM job_vacancies j);
    """)

    recreate_staging_github_jobs_table = ("""
        DROP TABLE IF EXISTS staging_github_jobs;
        CREATE TABLE staging_github_jobs (
            id VARCHAR(38) PRIMARY KEY,
            type VARCHAR(100),
            url VARCHAR(1000),
            created_at TIMESTAMP,
            company VARCHAR(500),
            company_url VARCHAR(1000),
            location VARCHAR(500),
            title VARCHAR(500),
            description VARCHAR(65535),
            how_to_apply VARCHAR(1000),
            company_logo VARCHAR(1000)
        );
    """)

    insert_into_staging_github_jobs_table = ("""
        INSERT INTO staging_github_jobs (
            id, type, url, created_at, company, company_url, 
            location, title, description, how_to_apply, company_logo
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s
        )
    """)

    select_companies_from_github_jobs = ("""
        SELECT DISTINCT
            t_tmp.company_id as id,
            sgj.company AS name,
            t_tmp.company_url as remote_url
        FROM 
            (
	           SELECT REPLACE(TRIM(regexp_replace(translate(
		                LOWER(company),
		                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
		                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
		            ), '[^a-z0-9\-]+', ' ')),' ', '-') as company_id,
		            MAX(id) AS job_id,
		            MAX(company_url) AS company_url
				FROM staging_github_jobs
				GROUP BY REPLACE(TRIM(regexp_replace(translate(
				                LOWER(company),
				                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
				                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
				            ), '[^a-z0-9\-]+', ' ')),' ', '-')
            ) t_tmp
            LEFT JOIN staging_github_jobs sgj ON (sgj.id = t_tmp.job_id)
        WHERE
            t_tmp.company_id NOT IN (SELECT id FROM companies);
    """)

    select_job_vacancies_from_github_jobs = ("""
        select distinct
            id as id,
            'github_jobs' as provider_id,
            id as remote_id_on_provider,
            url as remote_url,
            location as location,
            null as currency_code,
            REPLACE(TRIM(regexp_replace(translate(
                LOWER(company),
                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
            ), '[^a-z0-9\-]+', ' ')),' ', '-') as company_id,
            company as company_name,
            title as title,
            (description || '\n' || how_to_apply) as description,
            null as tags,
            CAST(null AS numeric) as salary,
            CAST(null AS numeric) as salary_max,
            CAST(null AS numeric) as salary_frequency,
            0 as has_relocation_package,
            created_at as published_at
        FROM
            staging_github_jobs
        WHERE id NOT IN (SELECT j.id FROM job_vacancies j);
    """)

    recreate_staging_landing_jobs_table = ("""
        DROP TABLE IF EXISTS staging_landing_jobs;
        CREATE TABLE staging_landing_jobs (
            id INT8 PRIMARY KEY,
            city VARCHAR(255),
            company_id INT8,
            country_code VARCHAR(5),
            country_name VARCHAR(255),
            currency_code VARCHAR(5),
            expires_at DATE,
            main_requirements VARCHAR(65535),
            nice_to_have VARCHAR(65535),
            perks VARCHAR(65535),
            referral_value VARCHAR(20),
            relocation_paid INT4,
            role_description VARCHAR(65535),
            title VARCHAR(500),
            created_at TIMESTAMP,
            updated_at TIMESTAMP,
            published_at TIMESTAMP,
            type VARCHAR(255),
            remote INT4,
            tags VARCHAR(65535),
            url VARCHAR(1000),
            gross_salary_low NUMERIC(18,2),
            gross_salary_high NUMERIC(18,2)
        );
    """)

    select_tags_from_landing_jobs = ("""
        SELECT DISTINCT s.token AS "tag"
        FROM   staging_landing_jobs t, unnest(string_to_array(t.tags, ',')) s(token)
        WHERE  LENGTH(s.token) <= 50 and s.token not in (select "tag" from tags);
    """)

    select_job_vacancies_from_landing_jobs = ("""
        select distinct
            id as id,
            'landing_jobs' as provider_id,
            id as remote_id_on_provider,
            url as remote_url,
            city || ', ' || country_name as location,
            currency_code as currency_code,
            company_id as company_id,
            null as company_name,
            title as title,
            (
                'Type: ' || type || '\n\n' || 
                role_description || '\n\n' || 
                main_requirements || '\n\n' || 
                nice_to_have || '\n\n' || 
                perks
            ) as description,
            tags as tags,
            gross_salary_low as salary,
            gross_salary_high as salary_max,
            'anually' as salary_frequency,
            relocation_paid as has_relocation_package,
            TO_CHAR(expires_at, 'YYYY-MM-DD')::timestamp as expires_at,
            created_at as published_at
        FROM
            staging_landing_jobs
        WHERE CAST(id AS CHAR) NOT IN (SELECT j.id FROM job_vacancies j);
    """)

    insert_into_staging_landing_jobs_table = ("""
        INSERT INTO staging_landing_jobs (
            id, city, company_id, country_code, country_name, currency_code, expires_at, main_requirements, 
            nice_to_have, perks, referral_value, relocation_paid, role_description, title, created_at, 
            updated_at, published_at, type, remote, tags, url, gross_salary_low, gross_salary_high
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, %s, %s, %s
        )
    """)

    recreate_staging_stackoverflow_jobs_table = ("""
        DROP TABLE IF EXISTS staging_stackoverflow_jobs;
        CREATE TABLE staging_stackoverflow_jobs (
            id VARCHAR(50) PRIMARY KEY,
            remote_url VARCHAR(1000),
            location VARCHAR(500),
            company_name VARCHAR(1000),
            title VARCHAR(1000),
            description VARCHAR(65535),
            tags VARCHAR(65535),
            published_at TIMESTAMP
        );
    """)

    insert_into_staging_stackoverflow_jobs = ("""
        INSERT INTO staging_stackoverflow_jobs (
            id, remote_url, location, company_name, title, description, tags, published_at
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s
        )
    """)

    select_tags_from_stackoverflow_jobs = ("""
        SELECT DISTINCT s.token AS "tag"
        FROM   staging_stackoverflow_jobs t, unnest(string_to_array(t.tags, ',')) s(token)
        WHERE  LENGTH(s.token) <= 50 and s.token not in (select "tag" from tags);
    """)

    select_companies_from_stackoverflow_jobs = ("""
        SELECT DISTINCT
            t_tmp.company_id as id,
            sgj.company_name AS name,
            null as remote_url
        FROM 
            (
	           SELECT REPLACE(TRIM(regexp_replace(translate(
		                LOWER(company_name),
		                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
		                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
		            ), '[^a-z0-9\-]+', ' ')),' ', '-') as company_id,
		            MAX(id) AS job_id
				FROM staging_stackoverflow_jobs
				GROUP BY REPLACE(TRIM(regexp_replace(translate(
				                LOWER(company_name),
				                'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
				                'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
				            ), '[^a-z0-9\-]+', ' ')),' ', '-')
            ) t_tmp
            LEFT JOIN staging_stackoverflow_jobs sgj ON (sgj.id = t_tmp.job_id)
        WHERE
            t_tmp.company_id NOT IN (SELECT id FROM companies);
    """)

    select_job_vacancies_from_stackoverflow_jobs = ("""
        select distinct
            md5(id || '_stackoverflow_jobs') as id,
            'stackoverflow_jobs' as provider_id,
            id as remote_id_on_provider,
            remote_url as remote_url,
            location as location,
            null as currency_code,
            REPLACE(TRIM(regexp_replace(translate(
                        LOWER(company_name),
                        'áàâãäåāăąèééêëēĕėęěìíîïìĩīĭḩóôõöōŏőùúûüũūŭůäàáâãåæçćĉčöòóôõøüùúûßéèêëýñîìíïş',
                        'aaaaaaaaaeeeeeeeeeeiiiiiiiihooooooouuuuuuuuaaaaaaeccccoooooouuuuseeeeyniiiis'
                    ), '[^a-z0-9\-]+', ' ')),' ', '-') as company_id,
            company_name as company_name,
            title as title,
            description as description,
            tags as tags,
            CAST(null AS numeric) as salary,
            CAST(null AS numeric) as salary_max,
            CAST(null AS numeric) as salary_frequency,
            0 as has_relocation_package,
            published_at as published_at
        FROM
            staging_stackoverflow_jobs
        WHERE md5(id || '_stackoverflow_jobs') NOT IN (SELECT j.id FROM job_vacancies j);
    """)

    upsert_jobs_row = ("""
        INSERT INTO job_vacancies (
            id, provider_id, remote_id_on_provider, remote_url, location, 
            currency_code, company_id, company_name, title, description, 
            tags, salary, salary_max, salary_frequency, has_relocation_package, 
            expires_at, published_at
        )
        VALUES (
            %(id)s, %(provider_id)s, %(remote_id_on_provider)s, %(remote_url)s, %(location)s, 
            %(currency_code)s, %(company_id)s, %(company_name)s, %(title)s, %(description)s, 
            %(tags)s, %(salary)s, %(salary_max)s, %(salary_frequency)s, %(has_relocation_package)s, 
            %(expires_at)s, %(published_at)s
        )
        ON CONFLICT (id)
        DO UPDATE SET
            provider_id = job_vacancies.provider_id, 
            remote_id_on_provider = job_vacancies.remote_id_on_provider, 
            remote_url = job_vacancies.remote_url, 
            location = job_vacancies.location, 
            currency_code = job_vacancies.currency_code, 
            company_id = job_vacancies.company_id, 
            company_name = job_vacancies.company_name, 
            title = job_vacancies.title, 
            description = job_vacancies.description, 
            tags = job_vacancies.tags, 
            salary = job_vacancies.salary, 
            salary_max = job_vacancies.salary_max, 
            salary_frequency = job_vacancies.salary_frequency, 
            has_relocation_package = job_vacancies.has_relocation_package, 
            expires_at = job_vacancies.expires_at, 
            published_at = job_vacancies.published_at
    """)

    upsert_companies_row = ("""
        INSERT INTO companies (id, name, remote_url) VALUES (%(id)s, %(name)s, %(remote_url)s)
        ON CONFLICT (id)
        DO UPDATE SET
            name = companies.name, 
            remote_url = companies.remote_url
    """)

    upsert_tags_row = ("""
        INSERT INTO tags (tag) VALUES (%(tag)s)
        ON CONFLICT (tag) DO NOTHING
    """)
