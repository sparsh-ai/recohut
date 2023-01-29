DROP TABLE IF EXISTS dates cascade;
CREATE TABLE dates(
        date                   DATE          NOT NULL PRIMARY KEY SORTKEY,
        year                   INTEGER       NOT NULL
) DISTSTYLE ALL;


DROP TABLE IF EXISTS details cascade;
CREATE TABLE details(
        detail_id              VARCHAR(20)   NOT NULL PRIMARY KEY DISTKEY,
        title                  varchar(max)  NOT NULL,
        abstract               varchar(max)
);

DROP TABLE IF EXISTS owners cascade;
CREATE TABLE owners(
        owner_id               VARCHAR(64)   NOT NULL PRIMARY KEY,
        type                   VARCHAR(20)   NOT NULL,
        name                   VARCHAR(500)  NOT NULL
)DISTSTYLE ALL;

DROP TABLE IF EXISTS locations cascade;
CREATE TABLE locations(
        location_id            VARCHAR(64)   NOT NULL PRIMARY KEY,
        country                VARCHAR(200)  NOT NULL,
        continent              VARCHAR(200)  NOT NULL

)DISTSTYLE ALL;

DROP TABLE if exists wipo_classifications cascade;
CREATE TABLE wipo_classifications(
        wipo_classification_id INTEGER   NOT NULL PRIMARY KEY DISTKEY,
        sector                 VARCHAR(200)  NOT NULL,
        field                  VARCHAR(200)  NOT NULL
);

DROP TABLE if exists patent_keywords cascade;
CREATE TABLE patent_keywords(
        patent_keyword_id      VARCHAR(64)   NOT NULL PRIMARY KEY,
        patent_id              VARCHAR(20)   NOT NULL DISTKEY,
        keyword                VARCHAR(500)  NOT NULL
);

DROP TABLE IF EXISTS patents cascade;
CREATE TABLE patents(
        id                     VARCHAR(20)   NOT NULL PRIMARY KEY DISTKEY,
        granted_date           DATE          NOT NULL SORTKEY,
        detail_id              VARCHAR(20)   NOT NULL,
        owner_id               VARCHAR(64),
        location_id            VARCHAR(64),
        wipo_classification_id INTEGER,
        num_claims             INTEGER       NOT NULL
);

