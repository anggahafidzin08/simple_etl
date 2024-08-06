import os
import psycopg2 as pg
import json
import subprocess

def connect_vpn(config_file, credentials_file):
    try:
        with open(credentials_file) as f:
            data = json.load(f)['openvpn']
        
        # create temporary file.txt
        with open('temp_credentials.txt', 'w') as cred_file:
            cred_file.write(f"{data['username']}\n{data['password']}\n")
        print('running command')
        # Run the OpenVPN command with the given config file and credentials
        command = [
            "openvpn",
            "--config", config_file,
            "--auth-user-pass", "C:\\Users\\angga.hafidzin\\Data Business Intelligence\\Analysis\\Python Scripts\\B2B Dashboard Updates Documents\\temp_credentials.txt"
        ]
        print('use subprocess')
        # Use subprocess to execute the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Output for logging
        for line in iter(process.stdout.readline, b''):
            print(line.decode('utf-8').strip())

        process.stdout.close()
        process.wait()

        if process.returncode == 0:
            print("VPN connected successfully")
        else:
            print("Failed to connect VPN")

    except Exception as e:
        print(f"An error occurred: {e}")
    
def connect_db(creds, sub_data):
    with open(creds) as f:
        data = json.load(f)[sub_data]
    con = pg.connect("dbname={a} user={b} password={c} host={d} port={e}".format(a=data['DB_NAME'], b=data['DB_USER'], c=data['DB_PASSWORD']
                                                                             , d=data['DB_HOST'], e=data['DB_PORT']))
    cur = con.cursor()
    return con, cur;