
from fuel import convert, gauge


def test_0():
    assert convert("3/4") == "75"

def test_1():
    assert convert("1/1") == "100"

def test_2():
    assert convert("1/10?") == "10?"

# def test_3():
#     assert convert("TWITTER") == "TWTTR"

def test_4():
    assert gauge(75) == "75%"

def test_5():
    assert gauge(100) == "F"

def test_6():
    assert gauge(1) == "E"

# def test_7():
#     assert gauge("twit..ter") == "twt..tr"