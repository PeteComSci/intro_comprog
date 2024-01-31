# test_basic_if_elif_statements.py
import pytest
from conditional_statements import check_number

def test_positive_number():
    assert check_number(5) == "Positive"

def test_negative_number():
    assert check_number(-3) == "Negative"

def test_zero():
    assert check_number(0) == "Zero"

if __name__ == '__main__':
    pytest.main()
