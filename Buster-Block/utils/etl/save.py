import os
import pandas as pd
import log_control


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

    log_control.loggerETL.info(f'Start of file saving: {name}')
    try:
        # File path and folder to save
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'processed_data')
        # Full path
        file = root + '/' + name
        # Saved from df
        df.to_csv(file, index=False)
        log_control.loggerETL.info('Save successful!')

    except Exception as e:
        log_control.loggerETL.error(f'File saving error{e}')
