CREATE TABLE IF NOT EXISTS public.store_types
(
    "ID_Store_Type" integer NOT NULL,
    "Store_Type" character(20) COLLATE pg_catalog."default",
    CONSTRAINT store_types_pkey PRIMARY KEY (ID_Store_Type)
)