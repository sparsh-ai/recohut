CREATE TABLE dimDate
    (
      date_key integer NOT NULL PRIMARY KEY,
        date date NOT NULL,
        year smallint NOT NULL,
        quarter smallint NOT NULL,
        month smallint NOT NULL,
		week smallint NOT NULL,
        day smallint NOT NULL,
        is_weekend boolean
    );


insert into dimdate
	(date_key, date, year, quarter, month, week, day, is_weekend)
	select 
	distinct(to_char(payment_date :: Date, 'yyyymmdd'):: integer) as date_key,
	date(payment_date) as date,
	extract(year from payment_date) as year,
	extract(quarter from payment_date) as quarter,
	extract(month from payment_date) as month,
	extract(week from payment_date) as week,
	extract(day from payment_date) as day,
	case when extract(isodow from payment_date) in(6,7) then true else false end as is_weekend
	from payment;
	

DROP TABLE IF EXISTS dimcustomer;
CREATE TABLE dimcustomer
    (
      customer_key SERIAL PRIMARY KEY,
      customer_id  smallint NOT NULL,
      customer_first_name   varchar(45) NOT NULL,
      customer_last_name    varchar(45) NOT NULL,
      email        varchar(50),
      address      varchar(50) NOT NULL,
      address2     varchar(50),
      district     varchar(20) NOT NULL,
      city         varchar(50) NOT NULL,
      country      varchar(50) NOT NULL,
      postal_code  varchar(10),
      phone        varchar(20) ,
      create_date  timestamp NOT NULL,
      start_date   date NOT NULL,
      end_date     date NOT NULL
    );

insert into dimcustomer(customer_key, customer_id, customer_first_name, customer_last_name,
						email, address, address2, district, city, country, postal_code, 
					   create_date, start_date, end_date)
					   select 
					   c.customer_id as customer_key,
					   c.customer_id,
					   c.first_name,
					   c.last_name,
					   c.email,
					   a.address,
					   a.address2,
					   a.district,
					   ci.city,
					   co.country,
					   a.postal_code,
					   c.create_date,
					   now() as start_date,
					   now() as end_date
					   from customer c
					   join address a on (c.address_id = a.address_id)
					   join city ci on a.city_id = ci.city_id
					   join country co on ci.country_id = co.country_id;
					   
					   
					   
DROP TABLE IF EXISTS dimfilm;
CREATE TABLE dimfilm
    (
      movie_key          SERIAL PRIMARY KEY,
      film_id            smallint NOT NULL,
      title              varchar(255) NOT NULL,
      description        text,
      release_year       year,
      ratings             varchar(5) NOT NULL,
      language           varchar(20) NOT NULL,
      length             smallint NOT NULL,
    );
    
insert into dimfilm(film_key, film_id, title, description, 
					release_year, ratings, language, length)
			select 
			f.film_id as film_key,
			f.film_id,
			f.title,
			f.description,
			f.release_year,
			f.rating,
			l.name,
			f.length
			from film f left join language l
			on f.language_id = l.language_id;

DROP TABLE IF EXISTS dimstore;
CREATE TABLE dimStore
    (
      store_key           SERIAL PRIMARY KEY,
      store_id            smallint NOT NULL,
      address             varchar(50) NOT NULL,
      address2            varchar(50),
      district            varchar(20) NOT NULL,
      city                varchar(50) NOT NULL,
      country             varchar(50) NOT NULL,
      postal_code         varchar(10),
      manager_first_name  varchar(45) NOT NULL,
      manager_last_name   varchar(45) NOT NULL,
      start_date          date NOT NULL,
      end_date            date NOT NULL
    );			
insert into dimstore(store_key, store_id, address, address2,
					 district, city,country, postal_code, manager_first_name,
					manager_last_name, start_date, end_date)
					SELECT
					s.store_id as store_key,
					s.store_id,
					ad.address,
					ad.address2,
					ad.district,
					ci.city,
					co.country,
					ad.postal_code,
					st.first_name,
					st.last_name,
					now() as start_date,
					now() as end_date
					from store s 
					join staff st on st.staff_id = s.manager_staff_id
					join address ad on st.address_id = ad.address_id
					join city ci on ci.city_id = ad.city_id
					join country co on co.country_id = ci.country_id;
					

DROP TABLE IF EXISTS FACTSALES;
CREATE TABLE FACTSALES(
	sales_key serial primary key,
	date_key integer references dimdate(date_key),
	customer_key integer references dimcustomer(customer_key),
	film_key integer references dimfilm(film_key),
	store_key integer references dimstore(store_key),
	sales_amount numeric);
	
INSERT INTO factsales(date_key, customer_key, film_key,
					 store_key, sales_amount)
	SELECT
	TO_CHAR(payment_date :: date, 'yyyymmdd')::integer as date_key,
	p.customer_id as customer_key,
	i.film_id as film_key,
	i.store_id as store_key,
	p.amount as sales_amount
	from payment p
	join rental r on p.rental_id = r.rental_id
	join inventory i on r.inventory_id = i.inventory_id;


-- star schema
SELECT dimfilm.title, dimDate.month, dimCustomer.city, sum(sales_amount) as revenue
FROM factSales 
JOIN dimFILM    on (dimfilm.film_key      = factSales.film_key)
JOIN dimDate     on (dimDate.date_key         = factSales.date_key)
JOIN dimCustomer on (dimCustomer.customer_key = factSales.customer_key)
group by (dimfilm.title, dimDate.month, dimCustomer.city)
order by dimfilm.title, dimDate.month, dimCustomer.city, revenue desc;

-- 3nf model
-- 3nf
SELECT f.title, EXTRACT(month FROM p.payment_date) as month, ci.city, sum(p.amount) as revenue
FROM payment p
JOIN rental r    ON ( p.rental_id = r.rental_id )
JOIN inventory i ON ( r.inventory_id = i.inventory_id )
JOIN film f ON ( i.film_id = f.film_id)
JOIN customer c  ON ( p.customer_id = c.customer_id )
JOIN address a ON ( c.address_id = a.address_id )
JOIN city ci ON ( a.city_id = ci.city_id )
group by (f.title, month, ci.city)
order by f.title, month, ci.city, revenue desc;
