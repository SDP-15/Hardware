import serial
import re
import numpy as np
from tqdm import tqdm

# Global Variables
ser = serial.Serial("/dev/ttyACM0", 9600)  # "/dev/ttyACM0" for dice machine


def getData() -> list:
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


# Records around 2 readings a second
number_of_readings = 100

total_data = np.empty((0, 6), int)
for i in tqdm(range(number_of_readings)):
    data = getData()
    total_data = np.append(total_data, [data], axis=0)

file_name = "bad_test.npy"
with open(file_name, "wb") as f:
    np.save(f, total_data)
