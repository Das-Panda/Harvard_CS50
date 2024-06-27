import pytest
from Twttr import shorten

def test_shorten():
    # Test with a regular string
    assert shorten("Hello World") == "Hll Wrld"
    # Test with all vowels
    assert shorten("AEIOUaeiou") == ""
    # Test with no vowels
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
    # Test with an empty string
    assert shorten("") == ""
    # Test with a mix of upper and lower case
    assert shorten("AbCdEfGhIjK") == "bCdFghjK"
    # Test with special characters and spaces
    assert shorten("Th!s 1s @ test.") == "Th!s 1s @ tst."
    # Test with numeric values
    assert shorten("12345") == "12345"
    # Test with a mix of vowels, consonants, and special characters
    assert shorten("Twttr is c00l!") == "Twttr s c00l!"

if __name__ == "__main__":
    pytest.main()