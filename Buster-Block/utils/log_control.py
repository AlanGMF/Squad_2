import os
import logging
import logging.config

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'config/log_confi.conf')
logging.config.fileConfig(log_file_path)

loggerMain = logging.getLogger("loggerMain")
loggerETL = logging.getLogger("loggerETL")
loggerDB = logging.getLogger("loggerDB")