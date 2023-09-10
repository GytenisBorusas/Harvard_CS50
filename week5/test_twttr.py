
import pytest
from twttr import shorten


def test_shorten_function():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What is your name?") == "Wht's yr nm?"
