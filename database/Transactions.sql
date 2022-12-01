CREATE TABLE IF NOT EXISTS public.transactions
(
    id_transaction integer NOT NULL,
    id_customer integer,
    transaction_date date,
    id_subcategory integer,
    id_category integer,
    quantity numeric,
    rate numeric,
    tax numeric,
    total_amount numeric,
    id_store_type integer,
    id_product_category character(5) NOT NULL
    CONSTRAINT transactions_pkey PRIMARY KEY (id_transaction),
    CONSTRAINT category_fk FOREIGN KEY (id_product_category)
        REFERENCES public.product_categories (id_product_category) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT customer_fk FOREIGN KEY (id_customer)
        REFERENCES public.customers (id_customer) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT store_type_fk FOREIGN KEY (id_store_type)
        REFERENCES public.store_types (id_store_type) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)