.. module:: etl

ETL
===

Extraction module
-----------------
.. autofunction:: extraction.root_file()

Transformation module
---------------------
.. autofunction:: transform.standardization()
.. autofunction:: transform.df_prod()
.. autofunction:: transform.df_transactions()
.. autofunction:: transform.df_customers()
.. autofunction:: transform.no_change()

Save module
-----------
.. autofunction:: save.save_csv()