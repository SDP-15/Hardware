import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from typing import List, Tuple

class Visualizer:
    def __init__(self):
        self.sensors = []
        self.sensors.append(
            patches.Rectangle(
                (280, 100), 50, 50, linewidth=1, edgecolor="gray", facecolor="gray"
            )
        )
        self.sensors.append(
            patches.Rectangle(
                (355, 260), 50, 50, linewidth=1, edgecolor="gray", facecolor="gray"
            )
        )
        self.sensors.append(
            patches.Rectangle(
                (430, 100), 50, 50, linewidth=1, edgecolor="gray", facecolor="gray"
            )
        )
        self.sensors.append(
            patches.Rectangle(
                (355, 170), 50, 50, linewidth=1, edgecolor="gray", facecolor="gray"
            )
        )
        self.sensors.append(
            patches.Rectangle(
                (450, 340), 50, 50, linewidth=1, edgecolor="gray", facecolor="gray"
            )
        )
        self.sensors.append(
            patches.Rectangle(
                (430, 410), 50, 50, linewidth=1, edgecolor="gray", facecolor="gray"
            )
        )
        self.sensors.append(
            patches.Rectangle(
                (260, 340), 50, 50, linewidth=1, edgecolor="gray", facecolor="gray"
            )
        )
        self.sensors.append(
            patches.Rectangle(
                (280, 410), 50, 50, linewidth=1, edgecolor="gray", facecolor="gray"
            )
        )
        self.image = Image.open("officechair.png")

        # Create figure and axes
        self.fig, self.ax = plt.subplots()

        for sensor in self.sensors:
            self.ax.add_patch(sensor)

        # Display the image
        self.ax.imshow(self.image)
        plt.ion()
        plt.show()
        plt.draw()
        plt.pause(1)

    def update_values(self, data: List[Tuple[int, bool]]):
        """
        Updates the values that are used to visualise.

        :param data: List of sensor id, sensor reading pairs.
        """
        for sensor_id, active in data:
            color = "r" if active else "gray"
            self.sensors[sensor_id].set(edgecolor=color, facecolor=color)
        plt.draw()
        plt.pause(0.01)
