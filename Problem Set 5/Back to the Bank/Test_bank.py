import pytest
from Bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0

def test_value_h():
    assert value("hi") == 20
    assert value("Hi there") == 20
    assert value("howdy") == 20
    assert value("Hooray") == 20

def test_value_other():
    assert value("good morning") == 100
    assert value("Greetings") == 100
    assert value("What's up") == 100
    assert value("bye") == 100

if __name__ == "__main__":
    pytest.main()