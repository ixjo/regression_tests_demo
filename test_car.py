import logging

import pytest

from car import Car, prepare_car

# USEFUL LINKS:
# logging: https://docs.python.org/3/howto/logging.html
# pydantic: https://docs.pydantic.dev/latest/
# pytest: https://docs.pytest.org/en/7.1.x/index.html
# pytest-regressions: https://pytest-regressions.readthedocs.io/en/latest/overview.html


@pytest.fixture
def my_vw():
    """

    Fixtures in Pytest are a powerful mechanism to set up and provide data or resources needed for your tests.
    They allow you to define reusable components that can be automatically invoked by Pytest and shared across multiple test functions.

    To use a fixture, you can declare it by using the @pytest.fixture decorator before a function definition.
    When a test function includes a parameter with the same name as the fixture, Pytest automatically provides the fixture instance
    to the test function.

    Fixtures can be used for various purposes, such as setting up test data, initializing objects, or configuring the environment.
    They help in keeping your test code modular, clean, and DRY (Don't Repeat Yourself).

    This fixture initializes a Volkswagen car with specific parameters, including brand, empty weight, color,
    manufacturing year, and power.
    """
    return Car(
        brand="Volkswagen", empty_weight=1200, color="black", year=2019, power=150
    )


def test_if_car_is_black_unit(my_vw: Car):
    """
    Unit test to check if the car is black.

    Parameters:
    - my_vw: Instance of the Car class to be tested.

    The test prepares the car and then checks if its color attribute is set to "black."
    """
    # Prepare the car
    my_vw = prepare_car(my_vw)

    # Inspect the car
    assert my_vw.color == "black"


@pytest.mark.skip
def test_if_car_is_black_regression(my_vw, data_regression):
    """
    Regression test to check if the car object behaves as expected.

    Parameters:
    - my_vw: Virtual car instance to be tested.
    - data_regression: Fixture for regression testing of data output.

    The test prepares the virtual car, performs a drag race, and then inspects the car in its entirety.
    The resulting car information is checked against the expected output using the data_regression fixture.
    """

    # Prepare the car
    my_vw = prepare_car(my_vw)

    # Do a little drag race to test the car
    my_vw.gas_pedal(duration=3)

    # Inspect the car in its entirety
    car_dict = my_vw.model_dump()
    data_regression.check(car_dict)


@pytest.mark.skip
def test_logging_output(my_vw, file_regression, caplog):
    """
    Test the logging output of a virtual car during a test drive.

    Parameters:
    - my_vw: Virtual car instance to be tested.
    - file_regression: Fixture for regression testing of log output.
    - caplog: Fixture for capturing log output during the test.

    The test performs a test drive simulation by preparing the virtual car and accelerating for a duration of 3 seconds.
    The log output during this simulation is then checked against the expected log output using the file_regression fixture.
    """
    with caplog.at_level(logging.DEBUG):
        caplog.handler
        # Prepare the car
        my_vw = prepare_car(my_vw)
        # Do a little drag race to test the car
        my_vw.gas_pedal(duration=3)

    # check the logs
    text = "\n".join(log_record[2] for log_record in caplog.record_tuples)
    file_regression.check(text)
