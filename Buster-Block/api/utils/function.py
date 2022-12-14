import os
from pathlib import Path
DIR = os.path.dirname(os.path.normpath(__file__)).rstrip('/api/utils')
PATH_PROCESS_DATA = Path(__file__).parents[2].joinpath("utils").joinpath("etl").joinpath("processed_data")
PATH_RAW_DATA = Path(__file__).parents[2].joinpath("utils").joinpath("etl").joinpath("RAW_DATA")

def get_csv_files(path) -> list:
    """this function creates a list with the paths of the files

    :param path: file path to get name files
    :type path: str
    :return: the paths list
    :rtype: list
    """
    output_dir = f'{DIR}/utils/etl/processed_data/'
    rootDir = path

    for dirName, subdirList, fileList in os.walk(rootDir):
        filenames = []
        for fname in fileList:
            # append file path
            file_path = str(path.joinpath(fname))
            filenames.append(file_path)
            # filenames.append(output_dir + fname)

    return filenames
