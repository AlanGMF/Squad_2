-- public.store_types definition

-- Drop table

-- DROP TABLE public.store_types;

CREATE TABLE IF NOT EXISTS public.store_types (
	id_store_type serial4 NOT NULL,
	store_type varchar NULL,
	CONSTRAINT store_types_pkey PRIMARY KEY (id_store_type)
);