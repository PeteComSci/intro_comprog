# test_number_properties.py
import pytest
from number_properties import check_number_properties

def test_even_number():
    assert check_number_properties(4) == "Even"

def test_prime_number():
    assert check_number_properties(7) == "Prime"

def test_odd_number():
    assert check_number_properties(9) == "Odd"

if __name__ == '__main__':
    pytest.main()