import os

DIR = os.path.dirname(os.path.normpath(__file__)).rstrip('/api/utils')


def get_csv_files() -> list:
    """this function creates a list with the paths of the files

    :return: the paths list
    :rtype: list
    """
    output_dir = f'{DIR}/utils/etl/processed_data/'
    rootDir = output_dir

    for dirName, subdirList, fileList in os.walk(rootDir):
        filenames = []
        for fname in fileList:
            # append file path
            filenames.append(output_dir + fname)
    return filenames
