import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Any

def setup_logger() -> logging.Logger:
    """
    Configure and return a logger instance for image analysis.

    Returns:
        logging.Logger: The configured logger instance.
    """
    log = logging.getLogger("image_analysis")
    log.setLevel(logging.DEBUG)

    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "img_analayse.log") 
    file_handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=5)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    log.addHandler(file_handler)
    log.addHandler(console_handler)

    return log

log = setup_logger()
