-- public.transactions definition

-- Drop table

-- DROP TABLE public.transactions;

CREATE TABLE public.transactions (
	id_transaction serial4 NOT NULL,
	transaction_number numeric NULL,
	transaction_type varchar NULL,
	id_customer int4 NOT NULL,
	transaction_date date NULL,
	id_category int4 NOT NULL,
	id_subcategory int4 NOT NULL,
	quantity numeric NULL,
	rate numeric NULL,
	tax numeric NULL,
	total_amount numeric NULL,
	id_store int4 NOT NULL,
	id_store_type int4 NOT NULL,
	id_product_category varchar NOT NULL,
	CONSTRAINT transactions_pkey PRIMARY KEY (id_transaction)
);


-- public.transactions foreign keys

ALTER TABLE public.transactions ADD CONSTRAINT transactions_id_customer_fkey FOREIGN KEY (id_customer) REFERENCES public.customers(id_customer);
ALTER TABLE public.transactions ADD CONSTRAINT transactions_id_product_category_fkey FOREIGN KEY (id_product_category) REFERENCES public.product_categories(id_product_category);
ALTER TABLE public.transactions ADD CONSTRAINT transactions_id_store_fkey FOREIGN KEY (id_store) REFERENCES public.stores(id_store);
ALTER TABLE public.transactions ADD CONSTRAINT transactions_id_store_type_fkey FOREIGN KEY (id_store_type) REFERENCES public.store_types(id_store_type);
