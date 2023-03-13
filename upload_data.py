import serial
import mysql.connector
import time
import re
import sys
import database
from typing import Dict, Tuple

# Global Variables
ser = serial.Serial("COM7", 9600)  # "/dev/ttyACM0" for dice machine
db = database.DB()

def getData() -> dict:
    """
    Returns the latest reading for each sensor in a dictionary. Can be accessed by the id of the sensor.

    :return: dictionary with sensor id's as the keys and (sensor_id, sensor_reading, time_stamp) as the corresponding value
    """
    data = dict()
    while len(data) < 8:
        try:
            string = ser.readline().decode().strip()
            sensor_id, sensor_reading = re.search(
                r"reading(\d) = (\d+)", string
            ).groups()  # Sensor Id, pressure
            time_stamp = time.time()
            data[sensor_id] = (int(sensor_id), int(sensor_reading), time_stamp)
        except Exception as e:
            print(e)
            pass
    return data


def upload_data_to_db():
    """
    Upload the current sensor readings to the data base. Uploads once a second.
    """
    while True:
        data = getData()
        for _, value in data.items():
            string = f'INSERT INTO sensor_data (sensor_id, time_of_reading, reading) VALUES({value[0]}, "{value[2]}", {value[1]}) ON DUPLICATE KEY UPDATE time_of_reading="{value[1]}", reading={value[2]};'
            print(string)
            db.executeQuery(string)
        time.sleep(1)


upload_data_to_db()
