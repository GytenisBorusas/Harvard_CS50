


from response import validation_of_email


def test_1():
    assert validate("email") == "Invalid"
    
def test_2():
    assert validate("email.email.com") == "valid"

def test_3():
    assert validate("email@@@@gmail.com") == "Invalid"

def test_4():
    assert validate("gytenis@borusas..com") == "Invalid"


