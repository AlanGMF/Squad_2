import pandas as pd
from datetime import date
import etl.save as save

def standardization(dic_root: dict) -> None:
    """
    Calls the necessary functions for loading and saving CSV data 
    with the columns necessary for loading in the db

    :param dic_root: Dictionary with full paths
    :type dic_root: dict
    :return: None
    :rtype: None
    """

    for name in dic_root:
        # Selection of the df to work
        if name == 'prod_cat_info.csv' or name == 'transactions.csv':
            if name == 'prod_cat_info.csv':
                # Adding and saving column
                 df = df_prod(dic_root[name])
                 save.save_csv(name, df)
            else:
                # Adding and saving column
                df = df_transactions(dic_root[name])
                save.save_csv(name, df)
        else:
            if name == 'customer.csv':
                df = df_customers(dic_root[name])
                save.save_csv(name, df)
            else:
                df = no_change(dic_root[name])
                save.save_csv(name, df)


def df_prod(file: str) -> pd.DataFrame:
    """
    Performs the addition and normalization of the necessary csv

    :param file: file path
    :type file: str
    :return df: Modified DataFrame
    :rtype df: DataFrame
    """

    # File reading
    df = pd.read_csv(file)

    # Column aggregate
    df['id_product_category'] = df.prod_cat_code.apply(lambda x: str(x)) + "-" + df.prod_sub_cat_code.apply(lambda x: str(x))

    # Located in the first position of the df
    first_column = df.pop('id_product_category') 
    df.insert(0, 'id_product_category', first_column)

    # Normalize all column names
    df.rename(columns = {"id_product_category":"id_product_category"}, inplace = True)
    df.rename(columns = {"prod_cat_code":"id_category"}, inplace = True)
    df.rename(columns = {"prod_cat":"category"}, inplace = True)
    df.rename(columns = {"prod_sub_cat_code":"id_subcategory"}, inplace = True)
    df.rename(columns = {"prod_subcat":"subcategory"}, inplace = True)
    return df


def df_transactions(file: str) -> pd.DataFrame:
    """
    Performs the addition and normalization of the necessary csv

    :param file: file path
    :type file: str
    :return df: Modified DataFrame
    :rtype df: DataFrame
    """

    # File reading
    df = pd.read_csv(file)

    # Column aggregate
    df['id_product_category'] = df.prod_cat_code.apply(lambda x: str(x)) + "-" + df.prod_subcat_code.apply(lambda x: str(x))

    # Change type of tran_date column to datetime
    # The date is normalized to a single format. ("d/m/Y") -> ("d-m-Y")
    df['tran_date'] = df['tran_date'].replace("/", "-", regex=True)
    df[df['tran_date'].str.contains(r"-")]
    # Change type of tran_date to datetime
    df['tran_date'] = pd.to_datetime(df['tran_date'], format="%d-%m-%Y")

    # Integration of the corresponding type of transaction
    type_trans = df['Qty'].apply(lambda x: 'P' if x > 0 else 'R')
    df.insert(1,"transaction_type", type_trans)

    # Normalize all column names
    df.rename(columns = {"transaction_id":"transaction_number"}, inplace = True)
    df.rename(columns = {"cust_id":"id_customer"}, inplace = True)
    df.rename(columns = {"tran_date":"transaction_date"}, inplace = True)
    df.rename(columns = {"prod_subcat_code":"id_subcategory"}, inplace = True)
    df.rename(columns = {"prod_cat_code":"id_category"}, inplace = True)
    df.rename(columns = {"Qty":"quantity"}, inplace = True)
    df.rename(columns = {"Rate":"rate"}, inplace = True)
    df.rename(columns = {"Tax":"tax"}, inplace = True)
    df.rename(columns = {"total_amt":"total_amount"}, inplace = True)
    df.rename(columns = {"Store_type":"id_store_type"}, inplace = True)
    df.rename(columns = {"Store":"id_store"}, inplace = True)
    df.rename(columns = {"id_product_category":"id_product_category"}, inplace = True)
    return df


def df_customers(file: str) -> pd.DataFrame:
    """Normalization of CSV Customers"""

    # FIle reading
    df = pd.read_csv(file)

    # Change Obj's date of birth type to datetime
    df['DOB'] = pd.to_datetime(df['DOB'], format="%d-%m-%Y")

    # Fill null values 
    df.fillna(method="ffill", inplace= True)

    # Add Age column
    today = date.today()
    s_age = df['DOB'].apply(lambda x: today.year-x.year-((today.month, today.day)<(x.month, x.day)))
    df.insert(2, "age", s_age)

    # Normalize all column names
    df.rename(columns = {"customer_Id":"id_customer"}, inplace = True)
    df.rename(columns = {"DOB":"dob"}, inplace = True)
    df.rename(columns = {"Gender":"gender"}, inplace = True)
    df.rename(columns = {"city_code":"id_city"}, inplace = True)
    return df


def no_change(file: str) -> pd.DataFrame:
    """
    Save the csv without any changes

    :param file: file path
    :type file: str
    :return df: DataFrame without any change
    :rtype df: DataFrame
    """

    # File reading
    df = pd.read_csv(file)
    return df
