-- public.cities definition

-- Drop table

-- DROP TABLE public.cities;

CREATE TABLE IF NOT EXISTS public.cities (
	id_city serial4 NOT NULL,
	city varchar NULL,
	CONSTRAINT cities_pkey PRIMARY KEY (id_city)
);