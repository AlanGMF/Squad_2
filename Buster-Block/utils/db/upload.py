import os
import sys
import pandas as pd
sys.path.append('Buster-Block')
import utils.db.connect as db
import utils.db.models as models
import utils.log_control as log_control


def root_file() -> dict:
    """
    Gets the path of the CSV files and their respective name

    :return: root_file(Dictionary filename - path)
    :rtype: dict
    """

    log_control.loggerDB.info('Starting the directory extraction process')

    # Current work path
    root = str(os.path.abspath(os.getcwd()))
    root = root + "/Buster-Block/utils/etl/processed_data"
    log_control.loggerDB.info('Path obtained successfully!')

    # Route files
    files = os.listdir(root)
    log_control.loggerDB.info(f'Existing file path obtained successfully!')

    # Dictionary filename - path
    root_file = {}
    for f in files:
        root_file[f] = root + '/' + f

    log_control.loggerDB.info(f'Successful filename-path creation process!')
    return root_file


def create_db() -> None:
    """Creation of the database"""

    log_control.loggerDB.info('Beginning of the creation of the tables')
    try:
        db.Base.metadata.create_all(db.engine)
        log_control.loggerDB.info('Tables created successfully!')

    except Exception as e:
        msj = 'Failed to create tables successfully created, info: '
        log_control.loggerDB.error(f'{msj}{e}')
        return msj


def upload_csv(file: str, table: str) -> None:
    """
    Load dataframe to database

    :param file: CSV Directory
    :type file: str
    :param table: Table name
    :type table: str
    """

    log_control.loggerDB.info(f'Started the process of uploading data to the table: {table}')
    try:
        df = pd.read_csv(file)
        df.to_sql(table, db.engine, if_exists='append', index=False)
        log_control.loggerDB.info('Upload successfully!')

    except Exception as e:
        msj = 'Error in the process of uploading data to the table '
        log_control.loggerDB.error(f'{msj}{table}, info: {e}')
        return msj


def upload_city(dict_files: dict) -> None:
    """
    Load the df cities to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """
    try:
        table = 'cities'
        file = dict_files['cities.csv']
        upload_csv(file, table)
    except Exception as e:
        msj = 'Error uploading the cities table'
        log_control.loggerDB.error(f'{msj}, info: {e}')
        return msj


def upload_customers(dict_files: dict) -> None:
    """
    Load the df customers to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    try:
        table = 'customers'
        file = dict_files['customer.csv']
        upload_csv(file, table)
    except Exception as e:
        msj = 'Error uploading the customers table'
        log_control.loggerDB.error(f'{msj}, info: {e}')
        return msj


def upload_product_categories(dict_files: dict) -> None:
    """
    Load the df product_categories to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    try:
        table = 'product_categories'
        file = dict_files['prod_cat_info.csv']
        upload_csv(file, table)

    except Exception as e:
        msj = 'Error uploading the product_categories table'
        log_control.loggerDB.error(f'{msj}, info: {e}')
        return msj


def upload_store_types(dict_files: dict) -> None:
    """
    Load the df store_types to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    try:
        table = 'store_types'
        file = dict_files['store_types.csv']
        upload_csv(file, table)

    except Exception as e:
        msj = 'Error uploading the store_types table'
        log_control.loggerDB.error(f'{msj}, info: {e}')
        return msj


def upload_stores(dict_files: dict) -> None:
    """
    Load the df stores to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    try:
        table = 'stores'
        file = dict_files['stores.csv']
        upload_csv(file, table)

    except Exception as e:
        msj = 'Error uploading the stores table'
        log_control.loggerDB.error(f'{msj}, info: {e}')
        return msj


def upload_transactions(dict_files: dict) -> None:
    """
    Load the df transactions to the database

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    try:
        table = 'transactions'
        file = dict_files['transactions.csv']
        upload_csv(file, table)

    except Exception as e:
        msj = 'Error uploading the transactions table'
        log_control.loggerDB.error(f'{msj}, info: {e}')
        return msj


def drop_all_tables() -> None:
    """Drops all the tables related to the dataframe"""

    log_control.loggerDB.info('Dropping existing tables for data aggregation')
    try:
        models.Transactions.__table__.drop(db.engine)
        models.Store.__table__.drop(db.engine)
        models.StoreTypes.__table__.drop(db.engine)
        models.ProductCategories.__table__.drop(db.engine)
        models.Customers.__table__.drop(db.engine)
        models.Cities.__table__.drop(db.engine)
        log_control.loggerDB.info('successful drop!')

    except Exception as e:
        msj = 'Error in the drop of existing tables for data aggregation, info: '
        log_control.loggerDB.error(f'{msj}{e}')
        return msj


def read_upload_csv(dict_files: dict) -> None:
    """
    Makes the necessary calls to load all the dataframes

    :param dict_files: Dictionary with all CSVs to load
    :type dict_files: dict
    """

    log_control.loggerDB.info('Start uploading all files')

    drop_all_tables()
    create_db()
    upload_city(dict_files)
    upload_customers(dict_files)
    upload_product_categories(dict_files)
    upload_store_types(dict_files)
    upload_stores(dict_files)
    upload_transactions(dict_files)
    log_control.loggerDB.info('Upload of all files successful!')
