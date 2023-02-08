import pytest
import pratice


def test_select():
    expected = "Samsung SyncMaster 941BW"
    assert pratice.select() == expected

if __name__ == '__main__':
    pytest.main()