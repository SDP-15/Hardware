import serial
import re
import numpy as np
import tensorflow as tf
import numpy as np
import manual_classifier
from typing import List
import visualise
import database
from datetime import datetime

# Global Variables
db = database.DB()
ser = serial.Serial("/dev/ttyACM0", 9600)  # "/dev/ttyACM0" for dice machine
active_threshold = 300
vis = visualise.Visualizer()


def getData() -> List[int]:
    """
    Returns the latest reading for each sensor in a dictionary. Can be accessed by the id of the sensor.

    :return: dictionary with sensor id's as the keys and (sensor_id, sensor_reading, time_stamp) as the corresponding value
    """
    data = dict()
    while len(data) < 6:
        try:
            string = ser.readline().decode().strip()
            sensor_id, sensor_reading = re.search(
                r"reading(\d) = (\d+)", string
            ).groups()  # Sensor Id, pressure
            data[sensor_id] = (int(sensor_id), int(sensor_reading))
        except Exception as e:
            print(e)

            pass
    # Initialise with 0's
    ret_dat = [0, 0, 0, 0, 0, 0]
    for _, value in data.items():
        ret_dat[value[0]] = value[1]
    return ret_dat


def visualise_reading(data: List[int]):
    """
    Visualizes the current sensor readings.
    """
    data_correct_format = [
        (idx, value >= active_threshold) for idx, value in enumerate(data)
    ]
    vis.update_values(data_correct_format)


upload_data = False
run_neural_network = False
if run_neural_network:
    model = tf.keras.models.load_model("models/posture-model.h5")

while True:
    data = getData()
    if run_neural_network:
        score = model(np.array([data])).numpy()[0][0]
        reason = -1
    else:
        score, reason = manual_classifier.score_posture(data, active_threshold)
    print("Score: " + score)
    visualise_reading(data)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if upload_data:
        query = f"INSERT INTO score (score, timestamp, reason) VALUES({score}, '{timestamp}', {reason});"
        db.executeQuery(query)
