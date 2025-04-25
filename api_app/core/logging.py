import os
import logging
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv


def get_logger(logger_name: str, log_file: Optional[str] = None) -> logging.Logger:
    
    load_dotenv()
    
    log_directory = os.getenv('LOGGING_DIRECTORY', '../logs')
    
    if log_file is None:
        log_file = f"{logger_name}.log"

    log_dir_path = Path(log_directory)
    log_dir_path.parent.mkdir(parents=True, exist_ok=True)
    full_log_path = log_dir_path / log_file

    logger = logging.getLogger(logger_name)

    if logger.handlers:
        return logger

    is_debug = os.getenv("LITESTAR_DEBUG", False)

    log_level = logging.DEBUG if is_debug else logging.INFO
    logger.setLevel(log_level)

    if is_debug:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s"
        )
    else:
        formatter = logging.Formatter(
            "%(astime)s - %(name)s - %(levelname)s - %(message)s"
        )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(full_log_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
