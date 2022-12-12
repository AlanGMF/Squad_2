import os
import uvicorn
import logging
import time
from fastapi import FastAPI
from utils.function import get_csv_files
#from BusterBlock.utils.main import main

# directory
DIR = os.path.dirname(os.path.normpath(__file__))

# logging config
logging.config.fileConfig(
    f'{DIR}/config/api_log.cfg'
)

# get the logger
logger = logging.getLogger("api_logger")

app = FastAPI()


@app.get("/getdata")
def upload():
    """this endpoint returns all data paths to streamlit
    :return: data paths
    :rtype: string
    """
    #start etl
    #main()
    #time.sleep(5)

    # files paths
    paths_list = get_csv_files()

    try:
        return paths_list
    except Exception:
        logger.error("Api error", exc_info=True)


# main to run fastapi automatically
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
