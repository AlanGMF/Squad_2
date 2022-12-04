import os
import pandas as pd


def save_csv(name: str, df: pd.DataFrame) -> None:
    """
    Save the modified CSV files

    :param name: File name
    :type name: str
    :param df: DataFrame of the file
    :type df: DataFrame
    :return: None
    :rtype: None
    """
    # File path and folder to save
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset')
    # Full path
    file = root + '/' + name
    # Saved from df
    df.to_csv(file, index=False)
