-- public.stores definition

-- Drop table

-- DROP TABLE public.stores;

CREATE TABLE IF NOT EXISTS public.stores (
	id_store serial4 NOT NULL,
	store_name varchar NULL,
	CONSTRAINT stores_pkey PRIMARY KEY (id_store)
);