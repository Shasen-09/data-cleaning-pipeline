import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler


def setup_logger(name=__name__):
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    log_folder = Path('logs')
    log_folder.mkdir(exist_ok=True)
    log_file = log_folder / "app.log"

    formatter = logging.Formatter(
        "%(asctime)s | %(message)s"
    )

    timed_rotation = TimedRotatingFileHandler(
        log_file,
        when='S',
        interval=5,
        backupCount=3
    )
    timed_rotation.suffix = "%Y-%m-%d_%H-%M-%S"
    timed_rotation.setFormatter(formatter)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(timed_rotation)

    return logger
