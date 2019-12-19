import logging
from logging import handlers


def _my_log(name, filename, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = handlers.TimedRotatingFileHandler(filename=filename, when='midnight', interval=7, backupCount=7)
    handler.suffix = "backup-%Y%m%d-%H%M.log"
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    logger.addHandler(handler)
    return logger


def log(name=None, filename=None, level=None):
    name = name if filename else __name__
    filename = filename if filename else 'log_default.log'
    level = level if level else logging.INFO

    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = _my_log(name, filename, level)
            return func(logger, *args, **kwargs)

        return wrapper

    return decorator
