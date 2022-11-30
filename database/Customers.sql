CREATE TABLE IF NOT EXISTS public.customers
(
    id_customer integer NOT NULL,
    dob date,
    gender "char",
    id_city integer,
    CONSTRAINT customers_pkey PRIMARY KEY (id_customer)
)
