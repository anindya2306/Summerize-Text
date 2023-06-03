import os
from box.exceptions import BoxValueError
import yaml
from SummerizeText.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.
    Args:
      path_to_yaml (str): Path to the yaml file.

    Raises:
        ValueError: If the yaml file is empty.
        e: empty yaml file

    Returns:
     ConfigBox: ConfigBox object.
    """
    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories.
    Args:
      path_to_directories (list): List of directories to be created.
      verbose (bool, optional): Whether to print the log. Defaults to True.
    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"directory: {directory} created successfully")


@ensure_annotations
def get_size(path_to_file: Path) -> str:
    """
    Returns the size of a file in KB.
    Args:
      path_to_file (Path): Path to the file.
    """
    return f"~ {round(os.path.getsize(path_to_file) / 1024, 2)} KB"

