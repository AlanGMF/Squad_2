CREATE TABLE IF NOT EXISTS public.store_types
(
    id_store_type integer NOT NULL,
    store_type character(20) COLLATE pg_catalog."default",
    CONSTRAINT store_types_pkey PRIMARY KEY (id_store_type)
)