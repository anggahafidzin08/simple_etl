# Simple ETL from Datawarehouse into a Data Mart
This project will provide a table/data mart based on Analyst requirements. Their objective is to create a clear Dashboard regarding sales activity in Marketplace.

Okay, here is the step to make/run a **Simple ETL**
## Step 1: Preparation
Define what kind of tools, libraries, and environments that would be usefull to create an ETL pipeline.
In this project I prefer to use ***Python*** because it easy to develop (High Level Language). --> Prepare Libraries:
- Pandas
- Psycopg2-binary
- SQLAlchemy
- sqlparse

All Libraries that I need to support this project already compiled into '**requirements.txt**', you just run on your python environments 
```sh 
pip install -r requirements.txt
```

## Step 2: Connecting Python to Datawarehouse on PostgreSQL
In this repository didn't provide the credentials of that we used to connect python and datewarehouse, just fill your own credentials using this format:
```sh
{
    "marketplace_prod": {
        "DB_HOST": "",
        "DB_NAME": "",
        "DB_USER": "",
        "DB_PASSWORD": "",
        "DB_PORT": ""
    },
    "dwh": {
        "DB_HOST": "",
        "DB_NAME": "",
        "DB_USER": "",
        "DB_PASSWORD": "",
        "DB_PORT": ""
    }
}
```
Then you can use my python script '**config.py**' to connect your datawarehouse.

## Step 3: Extract Transform Load
Create a target table on the selected database, create SQL query to extract the information needed, and then load into a targeted table.
