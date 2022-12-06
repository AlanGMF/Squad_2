import os
import log_control

def root_file()-> dict:
    """Gets the path of the CSV files and their respective name

    :return: root_file(Dictionary filename - path)
    :rtype: dict
    """

    log_control.loggerETL.info('Starting the directory extraction process')
    try:
        # Current work path
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'raw_data')
        log_control.loggerETL.info('Path obtained successfully!')

    except Exception as e:
        log_control.loggerETL.error(f'Error getting address, info: {e}')

    try:
        # Route files
        files = os.listdir(root)
        log_control.loggerETL.info(f'Existing file path obtained successfully!')

    except Exception as e:
        log_control.loggerETL.error(f'Error getting file path present in folder, info: {e}')

    try:
        # Dictionary filename - path
        root_file = {}
        for f in files:
            root_file[f] = root + '/' + f

        log_control.loggerETL.info(f'Successful filename-path creation process!')
        return root_file

    except Exception as e:
        log_control.loggerETL.error(f'Error in the filename-path creation process, info: {e}')
