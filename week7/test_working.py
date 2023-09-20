


from working import convert


def test1():
    assert convert("1.2.3.4") is True

def test2():
    assert convert("1.2.3.cat") is False

def test3():
    assert convert("cat") is False

def test4():
    assert convert("275.1.1.1") is False


