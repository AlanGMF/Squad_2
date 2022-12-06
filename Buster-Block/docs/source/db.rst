Database
========

Upload module
-------------
.. py:function:: root_file()

    Gets the path of the CSV files and their respective name

    :return: root_file(Dictionary filename - path)
    :rtype: dict

.. py:function:: create_db()

    Creation of the database

.. py:function:: upload_csv()

    Load dataframe to database

    :param file: CSV Directory
    :type file: str
    :param table: Table name
    :type table: str

.. py:function:: upload_city()

    Load the df cities to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict

.. py:function:: upload_customers()

    Load the df customers to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict

.. py:function:: upload_product_categories()
    
    Load the df product_categories to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict

.. py:function:: upload_store_types()

    Load the df store_types to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict

.. py:function:: upload_stores()
        
    Load the df stores to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict

.. py:function:: upload_transactions()

    Load the df transactions to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict

.. py:function:: drop_all_tables()

    Drops all the tables related to the dataframe

.. py:function:: read_upload_csv()

    Makes the necessary calls to load all the dataframes

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict

