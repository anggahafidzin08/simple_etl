import os
import psycopg2 as pg
import json
import subprocess
    
def connect_db(creds, sub_data):
    with open(creds) as f:
        data = json.load(f)[sub_data]
    con = pg.connect("dbname={a} user={b} password={c} host={d} port={e}".format(a=data['DB_NAME'], b=data['DB_USER']
                                , c=data['DB_PASSWORD'], d=data['DB_HOST'], e=data['DB_PORT']))
    cur = con.cursor()
    return con, cur;