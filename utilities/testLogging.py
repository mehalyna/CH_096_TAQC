"""Logging"""
import logging
import os
import datetime


class PyLogging():
    """
    Logging for Pytests
    Class attributes:
    debugs - a list of all devug messages
    infos - a list of all info messages
    warnings - a list of all warning messages
    criticals - a list of all critical messages
    Class methods:
    __init__() - constructor for initialize a logger with two output streams (console and file).
    Console Handler starts from DEBUG level
    File Handler starts from INFO level
    sendreport() - function for sending all logs from lists at once.
    debug() , info() , warning() , error() , critical() - functions for recording logs as they become available.
    exception() - function to record console traces into new .log file.
    """
    debugs = []
    infos = []
    warnings = []
    errors = []
    criticals = []

    def __init__(self, test_name="log"):
        """Constructor"""
        self.test_name = test_name
        self.logger = logging.getLogger(self.test_name)
        now = datetime.datetime.now()
        self.time = '{}.{}.{}'.format(now.day, now.month, now.year)
        self.dir = os.path.join(
            os.path.normpath(
                os.getcwd() +
                os.sep +
                os.pardir),
            'logs')
        print("logs directory:", self.dir)
        self.log_fname = os.path.join(
            self.dir, '{}-{}.log'.format(self.test_name, self.time))
        print("Log file:", self.log_fname)
        # self.logtrace_fname = os.path.join(
        #    self.dir, '{}-Traceback-{}.log'.format(self.test_name, self.time))
        #self.f_trace_handler = logging.FileHandler(self.logtrace_fname)
        self.c_handler = logging.StreamHandler()
        self.f_handler = logging.FileHandler(self.log_fname)
        self.c_handler.setLevel(logging.DEBUG)
        self.f_handler.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)
        self.c_format = logging.Formatter(
            '%(process)s - %(asctime)s - %(levelname)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S')
        self.f_format = logging.Formatter(
            '%(process)s - %(asctime)s - %(levelname)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S')
        self.c_handler.setFormatter(self.c_format)
        self.f_handler.setFormatter(self.f_format)
        self.logger.addHandler(self.c_handler)
        self.logger.addHandler(self.f_handler)
        self.log_file = open(self.log_fname, 'a')
        self.log_file.write("\n\n")

    def sendreport(self):
        """
        Function for sending all logs from lists at once.
        Args:
            param(PyLogging)
        """
        for i in self.debugs:
            self.logger.exception()
            self.logger.debug(i)
        for i in self.infos:
            self.logger.info(i)
        for i in self.warnings:
            self.logger.warning(i)
        for i in self.errors:
            self.logger.error(i)
        for i in self.criticals:
            self.logger.critical(i)

    def debug(self, deb):
        """
        :param deb (str): DEBUG message
        """
        self.logger.debug(deb)

    def info(self, inf):
        """
        :param inf (str): INFO message
        """
        self.logger.info(inf)

    def warning(self, war):
        """
        :param war (str): WARNING message
        """
        self.logger.warning(war)

    def error(self, err):
        """
        :param err (str): ERROR message
        """
        self.logger.error(err)

    def critical(self, cri):
        """
        :param cri (str): CRITICAL message
        """
        self.logger.critical(cri)

    def exception(self, mes):
        """
        Function to record console traces into new .log file.
        """

        logger = logging.getLogger(self.test_name + "Trace")
        self.logtrace_fname = os.path.join(
            self.dir, '{}-Traceback-{}.log'.format(self.test_name, self.time))
        self.f_trace_handler = logging.FileHandler(self.logtrace_fname)
        self.f_trace_handler.setLevel(logging.ERROR)
        self.f_trace_handler.setFormatter(self.f_format)
        logger.addHandler(self.f_trace_handler)
        self.logger.info("Traceback path: {}".format(self.logtrace_fname))
        self.log_file = open(self.logtrace_fname, 'a')
        self.log_file.write("\n\n")
        logger.exception(mes)
