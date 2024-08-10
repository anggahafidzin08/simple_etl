import config
import pandas as pd
import datetime
import os
import sqlparse

if __name__ == "__main__":
    # connect to prod database
    creds_mp = config.get_creds('credentials.json', 'marketplace_prod')
    conn_mp, engine_mp = config.connect_db(creds_mp)
    cur_mp = conn_mp.cursor()

    # connect to dmart database
    creds_dwh = config.get_creds('credentials.json', 'dwh')
    conn_dwh, engine_dwh = config.connect_db(creds_dwh)
    cur_dwh = conn_dwh.cursor()

    # get query
    path_query = os.getcwd() + '/query/'
    simple_etl = sqlparse.format(open(path_query+'query_simple_etl.sql'
                    , 'r').read()
                    , strip_comments=True).strip()
    print('[INFO] {a}: Succesfully fetched query_simple_etl.sql'.format(
            a=datetime.datetime.now()))
    create_table = sqlparse.format(open(path_query+'create_orders_table.sql'
                    , 'r').read()
                    , strip_comments=True).strip()
    print('[INFO] {a}: Succesfully fetched create_orders_table.sql'.format(
            a=datetime.datetime.now()))

    # execute query
    try:
        # simple etl
        dmart = pd.read_sql_query(simple_etl, engine_mp)
        print('[INFO] {a}: Succesfully exctract data from Marketplace DB'.format(
            a=datetime.datetime.now()))

        # create table
        cur_dwh.execute(create_table)
        conn_dwh.commit()
        print('[INFO] {a}: Succesfully Created dmart_orders_angga on DWH DB'.format(
            a=datetime.datetime.now()))

        dmart.to_sql(
            'dmart_orders_angga'
            , engine_dwh
            , schema='public'
            , if_exists='append'
            , index=False
        )
        print('[INFO] {a}: Succesfully ingest data to dmart_orders_angga'.format(
            a=datetime.datetime.now()))
    except Exception as e:
        print('[INFO] {a}: ERROR'.format(a=datetime.datetime.now()))
        print(str(e))