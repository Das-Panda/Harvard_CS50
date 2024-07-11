from um import count

def test_single_um():
    assert count("hello, um, world") == 1

def test_multiple_ums():
    assert count("um, well, um, that's interesting") == 2

def test_no_um():
    assert count("yummy") == 0

def test_case_insensitivity():
    assert count("UM, um, Um") == 3

def test_um_with_punctuation():
    assert count("Um... what are you saying?") == 1

def test_um_within_words():
    assert count("yummy, umbrella") == 0