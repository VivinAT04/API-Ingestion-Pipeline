import logging
import sys


LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s | "
    "%(filename)s:%(lineno)d | %(message)s"
)


def setup_logger(name: str = "api_ingestion_pipeline") -> logging.Logger:
    """
    Create a structured application logger for the ingestion pipeline.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))

    logger.addHandler(handler)
    logger.propagate = False

    return logger


logger = setup_logger()
