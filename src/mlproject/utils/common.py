import os
from box.exceptions import BoxValueErrror 
import yaml
from src.mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
       path_to_yaml(str): path like input

    Raises: 
       ValueError: if yamll file is empty
       e: empty file

    Returns: 
    ConfigBox : ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml file:
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file :{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
      path_to_directories(list):list of path diretories
      ingonre_log(bool.optional): ignore multiple directories is to created. dafault to
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)
        if verbose:
            logger.info(f"created directory at : {path}")


@ensure ensure_annotations

def save_json(path:Path, data: dict):
    """ save json data

    Args:
      path(Path): path to json file
      data(dict): data save in json file
      """

   with open(path, "w") as f:
     json.dump(data, f, indent=4)

    logger.info(f"json file save at: {path}")

@ensure_annotations

def load_json(path:Path) -> ConfigBox:
    """load json file data

    Args:
      path(Path) : path to json file

      Returns : 
        ConfigBox: data as class attributs instead of of dict

    """
    with open(Path) as f:
        content = json.load(f)

    logger.info(f""json file loaded successfully from : Path):
       return ConfigBox(content)


@ensure_annotations

def save_bin(data : Any, path : Path):
    """ save binary files

    Args:
      data(Any) : data to daved as binary
      path (Path): path to binary file

    """
    joblib.dump(value=data. filename=path)
    logger.info(f"banary file saved at : {path}")

@ensure_annotations

def load_bin(path : Path) -> Any:

    """load binary data

    Args:
    path(Path) : path to binary files

    Returns:

     Any : onject stored in files

     """
     data = joblib.load(path)

     logger.info(f"bianry file loaded from : {path}")
     return data


@ensure_annotations

def get_size(path : Path) -> str

   """ get size in kb

   Args :
    path(Path): path of the file

    Return : 
      str : size in kb
    """

    size_in_kb =round(os.path.getsize(path)/1024)
     return f"~ { size_in_kb} KB"








