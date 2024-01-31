# test_temperature_checker.py
import pytest
from temperature_checker import check_temperature

def test_hot_temperature():
    assert check_temperature(35) == "Hot"

def test_warm_temperature():
    assert check_temperature(25) == "Warm"

def test_cold_temperature():
    assert check_temperature(10) == "Cold"

if __name__ == '__main__':
    pytest.main()
