# -*- coding: UTF-8 -*-
"""
日志文件的操作
日志文件写入到 my.log中
"""


import logging
import logging.handlers
import datetime

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# 正确日志文件的保存位置
FILE_PATH = "my.log"
# 错误日志文件保存位置
FILE_ERR_PATH = "my.log.wf"


class ScanLog(object):
    """写入日志文件类"""
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.INFO)

    rf_handler = logging.handlers.TimedRotatingFileHandler(FILE_PATH,
                                    when='midnight', interval=1, backupCount=7)
    #filter = logging.Filter("ERROR")
    rf_handler.setLevel(logging.INFO)
    #rf_handler.addFilter(filter)
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler(FILE_ERR_PATH)
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s"
                                " - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)

    @classmethod
    def scan_info(cls, msg):
        """写入正确级别的日志"""

        cls.logger.info(msg)


    @classmethod
    def scan_err(cls, msg):
        """写入错误级别的日志"""

        cls.logger.error(msg)



