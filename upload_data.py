import serial
import mysql.connector
import time
import re
import sys
import visualise
from typing import Dict, Tuple

# Global Variables
ser = serial.Serial("COM7", 9600)  # "/dev/ttyACM0" for dice machine
# We consider a sensor to be active if the reading is more than or equal to 300
active_threshold = 300

# Sensor ids
back_top_left = 0
back_top_right = 1
back_middle_middle = 2
back_bottom_middle = 3
seat_back_left = 4
seat_back_right = 5
seat_front_left = 6
seat_front_right = 7


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


def visualise_readings():
    """
    Visualizes the current sensor readings.
    """
    vis = visualise.Visualizer()
    while True:
        data = getData()
        data_correct_format = [
            (value[0], value[1] >= active_threshold) for _, value in data.items()
        ]
        vis.update_values(data_correct_format)
        score = score_posture(data)
        print(score)


def score_posture(data: Dict[str, Tuple[int, int, str]]) -> int:
    data_formatted = {
        value[0]: value[1] >= active_threshold for _, value in data.items()
    }
    sitting = is_sitting(data_formatted)
    score = 1
    if not sitting:
        return score
    if not data_formatted[seat_front_right]:  # Right leg crossed over left
        score -= 0.25
        print("Right leg crossed over left leg.")
    if not data_formatted[seat_front_left]:  # Left leg crossed over right
        score -= 0.25
        print("Left leg crossed over right leg.")
    if (
        not data_formatted[seat_back_left]
        or not data_formatted[seat_back_right]
        or not data_formatted[back_bottom_middle]
    ):  # Slouching
        score -= 0.25
        print("You are slouching.")
    if (
        not data_formatted[back_top_left] or not data_formatted[back_top_right]
    ):  # Hunching
        score -= 0.25
        print("You are hunching forward.")
    return max(score, 0)  # should not be less than 0


def is_sitting(data: Dict[int, bool]) -> bool:
    """
    Returns true if we consider someone to be sitting on the chair.

    :param data: dictionary mapping from the sensor id to its reading.
    """
    return (
        data[seat_back_left]
        or data[seat_back_right]
        or data[seat_front_left]
        or data[seat_front_right]
    )


def upload_data_to_db():
    """
    Upload the current sensor readings to the data base. Uploads once a second.
    """
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
    else:
        sys.exit("Can't connect to db")

    while True:
        data = getData()
        for _, value in data.items():
            string = f'INSERT INTO sensor_data (sensor_id, time_of_reading, reading) VALUES({value[0]}, "{value[2]}", {value[1]}) ON DUPLICATE KEY UPDATE time_of_reading="{value[1]}", reading={value[2]};'
            print(string)
            cursor.execute(string)

        connection.commit()
        time.sleep(1)


should_vis = True
if should_vis:
    visualise_readings()
else:
    upload_data_to_db()
