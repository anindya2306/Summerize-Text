import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format= "[%(asctime)s]: %(message)s:")

project_name = "SummerizeText"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",      #Whenever this constructor file is included we will considerit as local package                                        
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
] 

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "": # if file directory dos't exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # if file does not exist or it is empty the overwrite it
        logging.info(f"Creating file {filepath}")
        with open(filepath, "w") as f:
            #f.write("")
            pass
    
    else:
        logging.info(f"File {filepath} already exists")


#After creating the folder structure we have to set up our virtual environment
#This is recommended to be done before doing any project setup
#Create the virtual environment: conda create -n SumText python=3.8 -y
#Activate the virtual environment: conda activate SumText