""" This File creates the Skeleton of our project """

# Imports
import os
from typing import Set
from typing import Any
from pathlib import Path
import logging

# configuring the logging setups
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] : %(message)s'
)

# Adding the Setups / Constants
PROJECT_NAME: str = 'CNN_Classifier'
LIST_OF_FILES: Set[str] = {

    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py",
    "templates/index.html"
}

for path in LIST_OF_FILES:
    path: Path = Path(path)
    file_dir: str= os.path.split(path)[0]
    filename: str=os.path.split(path)[1]

    # creating the directories
    if file_dir != "" :
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating Directory {file_dir} for the File {filename}")

    if (not os.path.exists(path)) or (os.path.getsize(path) == 0) :
        with open(path, 'w') as f:
            logging.info(f"Creating Empty File: {path}")
            pass

    else:
        logging.info(f"{filename} already exists")
