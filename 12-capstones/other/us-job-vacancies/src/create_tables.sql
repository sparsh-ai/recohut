drop table if exists public.job_vacancies;
CREATE TABLE public.job_vacancies (
	id VARCHAR(255) NOT NULL,
	provider_id VARCHAR(255) NOT NULL,
	remote_id_on_provider VARCHAR(500),
	remote_url VARCHAR(500),
	location VARCHAR(255),
	currency_code VARCHAR(3) DEFAULT NULL,
	company_id VARCHAR(500),
	company_name VARCHAR(500),
	title VARCHAR(1000),
	description VARCHAR(65535),
	tags VARCHAR(65535) DEFAULT NULL,
	salary NUMERIC(18,2) DEFAULT NULL,
	salary_max NUMERIC(18,2) DEFAULT NULL,
	salary_frequency VARCHAR(50) DEFAULT NULL,
	has_relocation_package INT4 DEFAULT NULL,
	expires_at TIMESTAMP DEFAULT NULL,
	published_at TIMESTAMP,
	CONSTRAINT job_vacancies_pkey PRIMARY KEY (id)
);

drop table if exists public.companies;
CREATE TABLE public.companies (
    id VARCHAR(500) NOT NULL,
    name VARCHAR(500),
    remote_url VARCHAR(500) DEFAULT NULL,
	CONSTRAINT companies_pkey PRIMARY KEY (id)
);

drop table if exists public.tags;
CREATE TABLE public.tags (
    "tag" VARCHAR(255) NOT NULL,
	CONSTRAINT tags_pkey PRIMARY KEY ("tag")
);


