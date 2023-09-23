


from seasons import calculation
from seasons import format_time


def test_1():
    assert calculation(2023, 9, 21) == ("One thousand, four hundred forty")

def test_2():
    assert calculation(2023, 9, 1) == ("Thirty thousand, two hundred forty")

# def test_3():
#     assert format_time("cat") is False

# def test_4():
#     assert format_time("275.1.1.1") is False