import utils.process_etl as etl
import logging

try:
  logger_main = logging.getLogger('main')
  logger_main.info('Starting the ETL process')
  etl.main()
except  Exception:
  logger_main.error("database query failed")
    