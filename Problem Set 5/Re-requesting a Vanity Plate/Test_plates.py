import pytest
from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAAAAAA") == False

def test_start_with_letters():
    assert is_valid("12ABCD") == False
    assert is_valid("AB1234") == True
    assert is_valid("A1BCDE") == False

def test_alphanumeric():
    assert is_valid("AB@CDE") == False
    assert is_valid("AB1234") == True
    assert is_valid("ABC123") == True

def test_number_position():
    assert is_valid("ABC123") == True
    assert is_valid("AB1234") == True
    assert is_valid("AB12CD") == False
    assert is_valid("AB0123") == False

if __name__ == "__main__":
    pytest.main()