CREATE TABLE IF NOT EXISTS public.transactions
(
    "ID_Transaction" integer NOT NULL,
    "ID_Customer" integer,
    "Transaction_Date" date,
    "ID_Subcategory" integer,
    "ID_Category" integer,
    "Quantity" numeric,
    "Rate" numeric,
    "Tax" numeric,
    "Total_Amount" numeric,
    "ID_Store" integer,
    "ID_Store_Type" integer,
    "ID_Product_Category" character(5) NOT NULL
    CONSTRAINT transactions_pkey PRIMARY KEY (id_transaction),
    CONSTRAINT category_fk FOREIGN KEY (id_product_category)
        REFERENCES public.product_categories (id_product_category) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT customer_fk FOREIGN KEY (id_customer)
        REFERENCES public.customers (id_customer) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT store_fk FOREIGN KEY (id_store)
        REFERENCES public.stores (id_store) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
    CONSTRAINT store_type_fk FOREIGN KEY (id_store_type)
        REFERENCES public.stpre_types (id_store_type) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)