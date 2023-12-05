import logging

import numpy as np
from pydantic import BaseModel

# USEFUL LINKS:
# logging: https://docs.python.org/3/howto/logging.html
# pydantic: https://docs.pydantic.dev/latest/
# pytest: https://docs.pytest.org/en/7.1.x/index.html
# pytest-regressions: https://pytest-regressions.readthedocs.io/en/latest/overview.html


class Car(BaseModel):
    brand: str
    empty_weight: float  # kg
    color: str
    year: int
    power: float  # kw
    speed: float = 0  # m/s

    def gas_pedal(self, duration=1):
        """
        This method simulates pressing the gas pedal of a car, increasing its speed based on the provided duration and power.

        Parameters:
        - duration (float, optional): The duration for which the gas pedal is pressed in seconds. Defaults to 1.

        Behavior:
        - Logs the information about pressing the gas pedal.
        - Calculates the change in kinetic energy based on the power and duration.
        - Updates the car's speed accordingly.
        """
        logging.info(f"Pressing the gas pedal for {duration} seconds!")
        delta_energy = self.power * duration * 1000  # J
        current_kinetic_energy = 0.5 * self.empty_weight * self.speed**2
        new_kinetic_energy = current_kinetic_energy + delta_energy
        new_speed = float(np.sqrt(2 * new_kinetic_energy / self.empty_weight))
        self.speed = new_speed

    def paint(self, color: str):
        """
        This method simulates painting the car with a specified color.

        Parameters:
        - color (str): The color to paint the car.

        """
        logging.info(f"Painting car {color}")
        self.color = color
        self.empty_weight += 1  # Paint adds to the weight


def prepare_car(car: Car) -> Car:
    # paint the car black using the 'Car.paint' method
    return car
