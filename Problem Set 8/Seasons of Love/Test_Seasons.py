from datetime import date
import pytest
from Seasons import calculate_age_in_minutes, convert_number_to_words

def test_calculate_age_in_minutes():
    # Test cases
    assert calculate_age_in_minutes(date(2000, 1, 1)) == (date.today() - date(2000, 1, 1)).days * 24 * 60
    assert calculate_age_in_minutes(date(1990, 5, 15)) == (date.today() - date(1990, 5, 15)).days * 24 * 60

def test_convert_number_to_words():
    # Test cases
    assert convert_number_to_words(525600) == "five hundred twenty five thousand six hundred"
    assert convert_number_to_words(1000000) == "one million"

if __name__ == "__main__":
    pytest.main()