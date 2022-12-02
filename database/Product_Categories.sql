-- public.product_categories definition

-- Drop table

-- DROP TABLE public.product_categories;

CREATE TABLE IF NOT EXISTS public.product_categories (
	id_product_category varchar NOT NULL,
	id_category int4 NOT NULL,
	category varchar NULL,
	id_subcategory int4 NOT NULL,
	subcategory varchar NULL,
	CONSTRAINT product_categories_pkey PRIMARY KEY (id_product_category)
);