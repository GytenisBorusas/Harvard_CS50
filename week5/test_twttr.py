
from twttr import shorten


def test_shorten_function():
    assert shorten("Twitter") == "Twttr"
    assert shorten("twitter") == "twttr"
    assert shorten("What is your name?") == "Whts yr nm?"
    assert shorten("TWITTER") == "TWTTR"

