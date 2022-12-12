import os
import uvicorn
import logging
from typing import Optional
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile

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
        print("no hay variables numericas")
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
    df = pd.read_csv(upload_file.file)
    upload_file.file.close()
    response= {}
    response["nulls"] = df.isnull().sum().to_dict()
    response["columns"] = df.columns.to_list()
    response["addfilter"] = get_numeric_columns(df)
    response["describe"] = df.describe().to_dict()

    return response

# main to run fastapi automatically
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
