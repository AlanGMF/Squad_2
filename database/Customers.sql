CREATE TABLE IF NOT EXISTS public.customers
(
    "ID_Customer" integer NOT NULL,
    "DOB" date,
    "Gender" "char",
    "ID_City" integer,
    CONSTRAINT customers_pkey PRIMARY KEY (id_customer)
)
