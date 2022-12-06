import os
import logging
import etl.extraction as extraction
import etl.transform as trasform
import db.upload as upload

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), './logs/main.log')

# Event logger
logging.basicConfig(filename=root, encoding='utf-8',
                    level=logging.DEBUG, datefmt='%y-%m-%d %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def main() -> None:
    """Call needed for the ETL process"""

# Management of the ETL process (locally)
    try:
        logging.info('Getting working directories')
        # Dictionary with full paths
        dic_root = extraction.root_file()

        logging.info('Working directory obtained successfully')

    except Exception as e:
        logging.error(f'Failed to get work path, info: {e}')
    
    try:
        logging.info('Normalization and saving to local CSV file started')
        # Normalization and saving to local CSV file
        trasform.standardization(dic_root)

        logging.info('Normalization and saving to local CSV file done successfully')

    except Exception as e:
        logging.error(f'Error in data normalization, info: {e}')

# Database management
    try:
        logging.info('Creating the databases')
        # Creation of the database
        upload.create_db()

        logging.info('Database created successfully')

    except Exception as e:
        logging.error(f'The database could not be created, information:{e}')

    try:
        logging.info('Starting to insert data into the database')
        # Starting data insertion
        dict_file = upload.root_file()
        upload.read_upload_csv(dict_file)

        logging.info('Starting data insert successful')

    except Exception as e:
        logging.error(f'Error trying to insert data, information:{e}')

if __name__ == '__main__':
    logging.info('Starting the ETL process')
    main()
