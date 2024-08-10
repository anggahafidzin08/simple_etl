import config
import pandas as pd
import numpy as np
import json
import os
import sqlparse

if __name__ == "__main__":
    # connect to database
    con, cur = config.connect_db('credentials.json', 'marketplace_prod')
    
    # mengambil sql query
    # path_query = os.getcwd()
    # query_stock = sqlparse.format(open(path_query + '\\stock_warehouse.sql', 'r').read(), strip_comments=True).strip()
    # stock = pd.read_sql(query_stock, con)
    # print(stock.head())
    print(pd.read_sql_query("""
        select *
        from marketplace.tb_orders
        order by 1
    """, con))
    con.close()
    cur.close()