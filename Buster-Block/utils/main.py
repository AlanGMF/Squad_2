import utils.etl.extraction as extraction
import utils.etl.transform as transform
import utils.log_control as log_control
import utils.db.upload as upload

def main() -> None:
    """Call needed for the ETL process"""

# Management of the ETL process (locally)
    try:
        log_control.loggerMain.info('Getting working directories')
        # Dictionary with full paths
        dic_root = extraction.root_file()

        log_control.loggerMain.info('Working directory obtained successfully')

    except Exception as e:
        log_control.loggerMain.error(f'Failed to get work path, info: {e}')
        return e
    
    try:
        log_control.loggerMain.info('Normalization and saving to local CSV file started')
        # Normalization and saving to local CSV file
        transform.standardization(dic_root)

        log_control.loggerMain.info('Normalization and saving to local CSV file done successfully')

    except Exception as e:
        log_control.loggerMain.error(f'Error in data normalization, info: {e}')
        return e

# Database management
    try:
        log_control.loggerMain.info('Creating the databases')
        # Creation of the database
        upload.create_db()

    except Exception as e:
        log_control.loggerMain.error(f'The database could not be created, information:{e}')
        return e

    try:
        log_control.loggerMain.info('Starting to insert data into the database')
        # Starting data insertion
        dict_file = upload.root_file()
        upload.read_upload_csv(dict_file)

        log_control.loggerMain.info('Starting data insert successful')

    except Exception as e:
        log_control.loggerMain.error(f'Error trying to insert data, information:{e}')
        return e

if __name__ == '__main__':
    log_control.loggerMain.info('Starting the ETL process')
    main()
