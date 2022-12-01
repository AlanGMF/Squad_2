CREATE TABLE IF NOT EXISTS public.product_categories
(
    "ID_Product_Category" character(5) NOT NULL,
    "ID_Category" integer NOT NULL,
    "Category" character(20) COLLATE pg_catalog."default",
    "ID_Subcategory" integer NOT NULL,
    "Subcategory" character(20) COLLATE pg_catalog."default",
    CONSTRAINT product_categories_pkey PRIMARY KEY (ID_Product_Category)
)