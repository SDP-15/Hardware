import serial
import re
import numpy as np
import tensorflow as tf
import numpy as np

# Global Variables
ser = serial.Serial("/dev/ttyACM0", 9600)  # "/dev/ttyACM0" for dice machine


def getData() -> list:
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
            data[sensor_id] = (int(sensor_id), int(sensor_reading))
        except Exception as e:
            print(e)

            pass
    # Initialise with 0's
    ret_dat = [0, 0, 0, 0, 0, 0, 0, 0]
    for _, value in data.items():
        ret_dat[value[0]] = value[1]
    return ret_dat


new_model = tf.keras.models.load_model("models/posture-model.h5")
while True:
    data = getData()
    print(new_model(np.array([data])))
