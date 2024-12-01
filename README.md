# CT80A0000 Data-Intensive Systems Assignment 4

### Requirements

This project needs the following

- docker
- docker compose
  - usually installed with docker
- python 3
- pip
  - usually installed with python3
- psycopg
  - this can be installed via pip with command `pip install "psycopg[binary]"`
- pymongo
  - this can be installed via pip with command `pip install "pymongo"`

### Instructions

To run this project be at the root folder and execute the following command `docker compose up -d`. This will start up the postgres and mongo databases that will run the init files located in `data` folder to populate them with sample data.

After the containers are up and running use the python executable to run the `frontend.py` file.
