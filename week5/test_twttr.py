
from twttr import shorten


def test_shorten_function():
    assert shorten("Twitter") == "Twttr"

def test_1():
    assert shorten("twitter") == "twttr"

def test_2():
    assert shorten("What is your name?") == "Wht s yr nm?"

def test_3():
    assert shorten("TWITTER") == "TWTTR"

def test_4():
    assert shorten("AEIOU") == ""

def test_5():
    assert shorten("AEIOUaeiou") == ""

def test_6():
    assert shorten("TWITTER123") == "TWTTR123"

def test_7():
    assert shorten("twit..ter") == "twt..tr"
