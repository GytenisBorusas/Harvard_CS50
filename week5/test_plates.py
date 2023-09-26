
from plates import is_valid


def test_is_valid1():
    assert shorten("CS50") == True

def test_is_valid2():
    assert shorten("CS05") == False

def test_is_valid3():
    assert shorten("PI3.14") == False

def test_is_valid4():
    assert shorten("H") == False

def test_is_valid5():
    assert shorten("OUTATIME") == False

