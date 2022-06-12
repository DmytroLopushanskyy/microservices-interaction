"""
Custom Logger class implementation
"""
import logging


class LogHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)
        logging.disable(logging.DEBUG)
        fmt = '%(asctime)s %(filename)-20s %(levelname)-10s: %(message)s'
        fmt_date = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)


LOGGER = logging.getLogger("root")
LOGGER.setLevel("INFO")
LOGGER.addHandler(LogHandler())
