import os
import json
import psycopg2 as pg
from sqlalchemy import create_engine
import datetime

def get_creds(creds, database):
    path = os.getcwd()
    with open(path+'/'+creds) as file:
        credents = json.load(file)[database]
    return credents;

def connect_db(credents):
    try:
        conn = pg.connect(
            host=credents['DB_HOST']
            , database=credents['DB_NAME']
            , user=credents['DB_USER']
            , password=credents['DB_PASSWORD']
            , port=credents['DB_PORT'])
        print('[INFO] {a}: Succesfully connected to {b}'.format(
            a=datetime.datetime.now(), b=credents["DB_NAME"]))
        engine = create_engine(
            "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
                credents['DB_USER']
                , credents['DB_PASSWORD']
                , credents['DB_HOST']
                , credents['DB_PORT']
                , credents['DB_NAME']
                )
        )
        print('[INFO] {a}: Succesfully create engine of {b}'.format(
            a=datetime.datetime.now(), b=credents["DB_NAME"]))
        return conn, engine
    except Exception as e:
        print('[INFO] Unsuccesfull')
        print(str(e))
        pass