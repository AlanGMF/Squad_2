import os
import uvicorn
import logging
from fastapi import FastAPI

# logging config
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s'
                    )

app = FastAPI()
DIR = os.path.dirname(os.path.normpath(__file__)).rstrip('/api')


@app.post("/getdata")
def upload():
    """this endpoint returns all data paths to streamlit
    :return: data paths
    :rtype: string
    """

    # files paths
    data_path1 = f"{DIR}/data/data/Customer.csv, {DIR}/data/data/dataframe_file.csv,"
    data_path2 = f"{DIR}/data/data/large_dff.csv, {DIR}/data/data/bici.csv"
    data_path = data_path1 + data_path2

    try:
        return data_path
    except Exception:
        logging.error("Api error", exc_info=True)


# main to run fastapi automatically
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
