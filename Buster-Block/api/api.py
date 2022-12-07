import os
import uvicorn
import logging
from fastapi import FastAPI

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


# main to run fastapi automatically
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
