import os
from pathlib import Path
DIR = os.path.dirname(os.path.normpath(__file__)).rstrip('/api/utils')
path_utils = Path(__file__).parents[2].joinpath("utils").joinpath("etl").joinpath("processed_data")

def get_csv_files() -> list:
    """this function creates a list with the paths of the files

    :return: the paths list
    :rtype: list
    """
    output_dir = f'{DIR}/utils/etl/processed_data/'
    rootDir = path_utils
    print(rootDir)
    for dirName, subdirList, fileList in os.walk(rootDir):
        filenames = []
        for fname in fileList:
            # append file path
            file_path = str(path_utils.joinpath(fname))
            filenames.append(file_path)
            # filenames.append(output_dir + fname)
    print(filenames)
    return filenames
