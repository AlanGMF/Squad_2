import os
import pandas as pd
import db.connect as db
import db.models as models


def root_file() -> dict:
    """
    Gets the path of the CSV files and their respective name

    :return: root_file(Dictionary filename - path)
    :rtype: dict
    """

    # Current work path
    root = str(os.path.abspath(os.getcwd()))
    root = root + "/utils/etl/dataset"

    # Route files
    files = os.listdir(root)

    # Dictionary filename - path
    root_file = {}
    for f in files:
        root_file[f] = root + '/' + f

    return root_file


def create_db() -> None:
    """Creation of the database"""
    db.Base.metadata.create_all(db.engine)


def upload_csv(file: str, table: str) -> None:
    """
    Load dataframe to database

    :param file: CSV Directory
    :type file: str
    :param table: Table name
    :type table: str
    """

    df = pd.read_csv(file)
    df.to_sql(table, db.engine, if_exists='append', index=False)


def uploat_city(dict_files) -> None:
    """
    Load the df cities to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    table = 'cities'
    file = dict_files['cities.csv']
    upload_csv(file, table)


def uploat_customers(dict_files) -> None:
    """
    Load the df customers to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    table = 'customers'
    file = dict_files['customer.csv']
    upload_csv(file, table)


def uploat_product_categories(dict_files) -> None:
    """
    Load the df product_categories to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    table = 'product_categories'
    file = dict_files['prod_cat_info.csv']
    upload_csv(file, table)


def uploat_store_types(dict_files) -> None:
    """
    Load the df store_types to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    table = 'store_types'
    file = dict_files['store_types.csv']
    upload_csv(file, table)


def uploat_stores(dict_files) -> None:
    """
    Load the df stores to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    table = 'stores'
    file = dict_files['stores.csv']
    upload_csv(file, table)


def uploat_transactions(dict_files) -> None:
    """
    Load the df transactions to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    table = 'transactions'
    file = dict_files['transactions.csv']
    upload_csv(file, table)


def drop_all_table() -> None:
    """Drops all the tables related to the dataframe"""

    models.Transactions.__table__.drop(db.engine)
    models.Store.__table__.drop(db.engine)
    models.StoreTypes.__table__.drop(db.engine)
    models.ProductCategories.__table__.drop(db.engine)
    models.Customers.__table__.drop(db.engine)
    models.Cities.__table__.drop(db.engine)


def read_upload_csv(dict_files: dict) -> None:
    """
    Makes the necessary calls to load all the dataframes

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    drop_all_table()
    create_db()
    uploat_city(dict_files)
    uploat_customers(dict_files)
    uploat_product_categories(dict_files)
    uploat_store_types(dict_files)
    uploat_stores(dict_files)
    uploat_transactions(dict_files)
