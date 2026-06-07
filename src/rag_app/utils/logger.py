import logging


def get_logger(name: str = __name__):
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)
