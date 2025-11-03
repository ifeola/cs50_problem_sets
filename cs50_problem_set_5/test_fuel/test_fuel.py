import pytest
from fuel import convert, gauge


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(10) == "10%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("3/4") == 75
    assert convert("0/4") == 0


def test_invalid_numb():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("three/four")
