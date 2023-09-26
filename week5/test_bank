

from bank import value


def test_value1():
    assert value("hello") == "$0"

def test_value2():
    assert value("harrrr") == "$20"

def test_value3():
    assert value("What a hell is this") == "$100"

def test_value4():
    assert value("But why") == "$100"