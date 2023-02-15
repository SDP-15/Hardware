import serial
from objprint import op
import mysql.connector
import time
import re
from datetime import datetime
import sys

ser = serial.Serial("COM7",9600)
server = 'sql8.freemysqlhosting.net'
database = 'sql8596986'
username = 'sql8596986'
password = 'zzRR3mNM8j'

connection = mysql.connector.connect(
    host=server,
    database=database, 
    user=username,
    password=password
)
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    query = """SELECT * FROM pressure_sensor_data"""

else:
    sys.exit("Can't connect to db")

while True:
    try:
        s = ser.readline().decode().strip()
        d = re.search(r'reading(\d) = (\d+)', s).groups()  # Sensor Id, pressure
        t = time.time()
        readable_t = datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
        print(
            f"INSERT INTO pressure_sensor_data (time, sensor_id, data) VALUES (\"{readable_t}\", \"{d[0]}\", \"{d[1]}\");")
        cursor.execute(
            f"INSERT INTO pressure_sensor_data (time, sensor_id, data) VALUES (\"{readable_t}\", \"{d[0]}\", \"{d[1]}\");")
        connection.commit()
    except Exception as e:
        print(e)
        pass
    
