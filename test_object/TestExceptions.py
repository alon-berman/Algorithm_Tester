import logging
import sys


class TestException(Exception):
    """
    Custom Error handler to properly attend issues occurring during run.
    """

    def __init__(self, msg, level=2, terminate=False):
        super(TestException, self).__init__(msg)
        logging.getLogger().setLevel(level * 10)
        logging.exception(msg)
        if terminate:
            sys.exit()
