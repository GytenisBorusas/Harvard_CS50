


from numb3rs import validate


def test1():
    assert validate("1.2.3.4") is True

def test2():
    assert validate("1.2.3.cat") is False

def test3():
    assert validate("cat") is False

def test4():
    assert validate("275.1.1.1") is False


