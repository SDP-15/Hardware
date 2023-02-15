import serial
import mysql.connector
import time
import re
from datetime import datetime
import sys
import visualise

ser = serial.Serial("COM7", 9600)
server = "sql8.freemysqlhosting.net"
database = "sql8596986"
username = "sql8596986"
password = "zzRR3mNM8j"

connection = mysql.connector.connect(
    host=server, database=database, user=username, password=password
)
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    query = """SELECT * FROM sensor_data"""

else:
    sys.exit("Can't connect to db")

values = dict()

should_vis = False
if should_vis:
    vis = visualise.Visualizer()
    values = []
while True:
    if should_vis:
        try:
            s = ser.readline().decode().strip()
            d = re.search(r"reading(\d) = (\d+)", s).groups()  # Sensor Id, pressure
            values.append((d[0], d[1]))
        except Exception as e:
            print(e)
            pass  
        if (len(values) == 8):
            vis.update_values(values)
            values = []
        continue

    try:
        s = ser.readline().decode().strip()
        d = re.search(r"reading(\d) = (\d+)", s).groups()  # Sensor Id, pressure
        t = time.time()
        readable_t = datetime.utcfromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")
        values[d[0]] = (d[0], t, d[1])
    except Exception as e:
        print(e)
        pass

    # Only push data once we have collected one datapoint per sensor
    if len(values.keys()) == 8:
        for _, value in values.items():
            string = f'INSERT INTO sensor_data (sensor_id, time_of_reading, reading) VALUES({value[0]}, "{value[1]}", {value[2]}) ON DUPLICATE KEY UPDATE time_of_reading="{value[1]}", reading={value[2]};'
            print(string)
            cursor.execute(string)

        connection.commit()
        time.sleep(1)
        values = dict()
