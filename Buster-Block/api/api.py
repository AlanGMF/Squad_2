import os
import uvicorn
import logging
from typing import Optional
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, Form
from pathlib import Path

# directory
DIR = os.path.dirname(os.path.normpath(__file__))

# logging config
logging.config.fileConfig(
    f'{DIR}/config/api_log.cfg'
)

# get the logger
logger = logging.getLogger("api_logger")

app = FastAPI()
DIR = os.path.dirname(os.path.normpath(__file__)).rstrip('/api') +"/utils/etl/process_data"
DIR_UTILS = Path(__file__).parents[1].joinpath("utils")
DIR_RAW_DATA = DIR_UTILS.joinpath("etl").joinpath("raw_data")


@app.get("/getdata")
def upload():
    """this endpoint returns all data paths to streamlit
    :return: data paths
    :rtype: string
    """

    # files paths
    data_path1 = f"{DIR}/cities.csv, {DIR}/customer.csv, {DIR}/transactions.csv,"
    data_path2 = f"{DIR}/prod_cat_info.csv, {DIR}/store_types.csv"
    data_path = data_path1 + data_path2

    try:
        return data_path
    except Exception:
        logger.error("Api error", exc_info=True)

class DataInsight(BaseModel):
    columns: list
    nulls: dict
    addfilter: Optional[dict] = None
    describe: dict

# ONE FILE

def get_numeric_columns(df:pd.DataFrame):
    """Gets the numeric columns with
     their maximum and minimum values

    :param df: pd.Dataframe
    :type df: pd.DataFrame
    :return: if the dataframe does not
        have numeric columns, it returns none,
        otherwise it returns a dataframe
        converted to a dictionary
    :rtype: dict | None
    """
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

    # get the minimum and maximum values
    max = df.select_dtypes(include=numerics).max()
    min = df.select_dtypes(include=numerics).min()

    # None is returned if there are
    # no maximums or minimums
    if max.empty or min.empty:
        # log (no numeric columns in df)
        return None
    else:
        # Both results are combined
        max_n_min = pd.concat([max, min], axis=1).to_dict()

    return max_n_min 


@app.post("/info_data", response_model=DataInsight)
async def get_file_info(upload_file: UploadFile):
    """returns a dictionary with information
    (null values, numeric columns, description)
    about the received df.

    :param upload_file: file to get data
    :type upload_file: UploadFile
    :return: data information
    :rtype: DataInsight
    """
    # Read data and save in raw_data folder
    df = pd.read_csv(upload_file.file)
    path = DIR_RAW_DATA.joinpath(upload_file.filename)
    df.to_csv(path)
    upload_file.file.close()

    # Get information
    response= {}
    response["nulls"] = df.isnull().sum().to_dict()
    response["columns"] = df.columns.to_list()
    response["addfilter"] = get_numeric_columns(df)
    response["describe"] = df.describe().to_dict()

    return response

@app.post("/transform_and_save")
async def transform_save_data(
    settings: str = Form(),
    save_file: bool = Form(),
    ):
    """receives a string parameter to apply
    changes to the dataset in the raw_data
    folder and returns the resulting dataset.

    :param settings: str(dict), defaults to Form()
    The form to receive has the following characteristics.

    {
        "file_name": str
        "slide_column_n":list[
                                0:float # min value
                                1:float # max value
                                ]
        "selec_columns":[
                        "column_1",
                        "column_2",
                        "column_n",
                        ]
        "nulls_action": "Delete rows" | "Nothing"
        "sort_column": "name_column"
        "order": "ASC" | "DESC"
    }

    :type settings: str, optional
    :param save_file: determines whether or not
        to save to the database, defaults to Form()
    :type save_file: bool, optional
    :return: dataframe with the changes applied
    :rtype: dict
    """
    # transform str in dict
    setting: dict
    setting = eval(settings)
    path = DIR_RAW_DATA.joinpath(setting["file_name"])

    # get df and filter by columns selected
    df = pd.read_csv(path).loc[:,setting["selec_columns"]]

    # drop nulls 
    if setting["selec_columns"] == "Delete rows":
        df.dropna(inplace=True)

    # sort by order and column
    order: bool
    if setting["order"] == "ASC":
        order = True
    else:
        order = False

    df.sort_values(
                setting["sort_column"],
                ascending= order,
                inplace=True
                )
    
    # get numeric columns to filter
    # apply filter in numeric columns

    for key in setting.keys():
        if "slide_" in key:

            # Remove the word slider_ from the column name
            column = key[6:]
            min = setting[key][0]
            max = setting[key][1]
            df = df[df[column].between(min, max)]

    return df.to_dict()


# main to run fastapi automatically
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
