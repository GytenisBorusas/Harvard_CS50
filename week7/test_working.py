


from working import convert


def test1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test2():
    assert convert("10:00 AM to 5:00 PM") == "10:00 to 17:00"

def test3():
    assert convert("11:00 AM to 6:00 PM") == "11:00 to 18:00"

def test4():
    assert convert("2:00 AM to 9:00 PM") == "02:00 to 21:00"


