"""Logging"""
import logging
import os
import datetime


def loger(file_name, lvl, message):
    """
    Logging for Pytests
    Console Handler starts from DEBUG level
    File Handler starts from INFO level
    sendreport() - function for sending all logs from lists at once.
    debug() , info() , warning() , error() , critical() - functions for recording logs as they become available.
    exception() - function to record console traces into new .log file.
    """
    test_name = file_name
    logger = logging.getLogger(test_name)
    now = datetime.datetime.now()
    time = '{}.{}.{}'.format(now.day, now.month, now.year)
    dir = os.path.join(
        os.path.normpath(
            os.getcwd() +
            os.sep +
            os.pardir),
        'Logs')
    print("Logs directory:", dir)
    log_fname = os.path.join(
        dir, '{}-{}.log'.format(test_name, time))
    print("Log file:", log_fname)
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(log_fname)
    c_handler.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)
    c_format = logging.Formatter(
        '%(process)s - %(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S')
    f_format = logging.Formatter(
        '%(process)s - %(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    log_file = open(log_fname, 'a')
    log_file.write("\n\n")
    if lvl.lower() == "debug":
        logger.debug(message)
    elif lvl.lower() == "info":
        logger.info(message)
    elif lvl.lower() == "warning":
        logger.warning(message)
    elif lvl.lower() == "error":
        logger.error(message)
    elif lvl.lower() == "critical":
        logger.critical(message)


if __name__ == '__main__':
    loger()
