import pytest
from Base import pratice

def test_title():
    exe="Your Store"
    assert pratice.title()==exe

if __name__ == '__main__':
    pytest.main()