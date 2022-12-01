CREATE TABLE IF NOT EXISTS public.product_categories
(
    id_product_category character(5) NOT NULL,
    id_category integer NOT NULL,
    category character(20) COLLATE pg_catalog."default",
    id_subcategory integer NOT NULL,
    subcategory character(20) COLLATE pg_catalog."default",
    CONSTRAINT product_categories_pkey PRIMARY KEY (id_product_category)
)