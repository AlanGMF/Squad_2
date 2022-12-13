import os
import utils.log_control as log_control

def root_file()-> dict:
    """Gets the path of the CSV files and their respective name

    :return: root_file(Dictionary filename - path)
    :rtype: dict
    """

    log_control.loggerETL.info('Starting the directory extraction process')
    
    # Current work path
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'raw_data')
    log_control.loggerETL.info('Path obtained successfully!')

    # Route files
    files = os.listdir(root)
    log_control.loggerETL.info(f'Existing file path obtained successfully!')
    
    # Dictionary filename - path
    root_file = {}
    for f in files:
        root_file[f] = root + '/' + f

    log_control.loggerETL.info(f'Successful filename-path creation process!')
    return root_file