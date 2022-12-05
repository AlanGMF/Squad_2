-- public.customers definition

-- Drop table

-- DROP TABLE public.customers;

CREATE TABLE IF NOT EXISTS public.customers (
	id_customer serial4 NOT NULL,
	dob date NULL,
	gender varchar NULL,
	age int4 NULL,
	id_city int4 NULL,
	CONSTRAINT customers_pkey PRIMARY KEY (id_customer)
);


-- public.customers foreign keys

ALTER TABLE public.customers ADD CONSTRAINT customers_id_city_fkey FOREIGN KEY (id_city) REFERENCES public.cities(id_city);
