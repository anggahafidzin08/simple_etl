import config
import pandas as pd
import numpy as np
import json
import os
import sqlparse

if __name__ == "__main__":
    # declare file path
    config_file = "C:\\Users\\angga.hafidzin\\Data Business Intelligence\\VPN Documents\\configla-prod.ovpn"
    credentials_file = "C:\\Users\\angga.hafidzin\\Data Business Intelligence\\Analysis\\Python Scripts\\B2B Dashboard Updates Documents\\db_creds.json"
    
    # connect to OpenVPN
    config.connect_vpn(config_file, credentials_file)
    
    # connect to database
#     con, cur = config.connect_db('db_creds.json', 'database')
    
#     # mengambil sql query
#     path_query = os.getcwd()
#     query_stock = sqlparse.format(open(path_query + '\\stock_warehouse.sql', 'r').read(), strip_comments=True).strip()
#     stock = pd.read_sql(query_stock, con)
#     print(stock.head())