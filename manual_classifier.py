import serial
import re
import visualise
from typing import List

# Global Variables
ser = serial.Serial("COM7", 9600)  # "/dev/ttyACM0" for dice machine

# Sensor ids
back_top_left = 0
back_top_right = 1
back_middle_middle = 2
back_bottom_middle = 3
seat_back_left = 4
seat_back_right = 5
seat_front_left = 6
seat_front_right = 7


def getData() -> List[int]:
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


def visualise_reading():
    """
    Visualizes the current sensor readings.
    """
    vis = visualise.Visualizer()
    data = getData()
    active_threshold = 300
    data_correct_format = [
        (idx, value >= active_threshold) for idx, value in enumerate(data)
    ]
    vis.update_values(data_correct_format)
    score = score_posture(data, active_threshold)
    print(score)


def score_posture(data: List[int], active_threshold: int) -> int:
    data_formatted = [value >= active_threshold for value in data]

    sitting = is_sitting(data_formatted)
    score = 1
    if not sitting:
        return score
    if not data_formatted[seat_front_left]:  # Left leg crossed over right
        score = 0
        print("Left leg crossed over right leg.")
    elif not data_formatted[seat_front_right]:  # Right leg crossed over left
        score = 0
        print("Right leg crossed over left leg.")
    if (
        not data_formatted[seat_back_left]
        or not data_formatted[seat_back_right]
        or not data_formatted[back_bottom_middle]
    ):  # Slouching
        score = 0
        print("You are slouching.")
    elif (
        not data_formatted[back_top_left] or not data_formatted[back_top_right]
    ):  # Hunching
        score = 0
        print("You are hunching forward.")
    return score


def is_sitting(data: List[bool]) -> bool:
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


if __name__ == "__main__":
    while True:
        visualise_reading()
