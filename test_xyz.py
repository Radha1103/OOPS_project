import spam
import pytest


def test_title():
    expected = "Your Store"
    assert spam.title() == expected
