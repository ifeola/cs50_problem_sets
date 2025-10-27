import pytest
from bank import value


def test_bak():
    assert value("Hello") == "$0"
    assert value("Hello, Newman") == "$0"
    assert value("How you doing?") == "$20"
    assert value("What's happening?") == "$100"
    assert value("What's up?") == "$100"


def test_spaces():
    assert value("Hello ") == "$0"
    assert value("   Hello  ") == "$0"


def test_lower():
    assert value("hello, world ") == "$0"


def test_numb():
    with pytest.raises(AttributeError):
        value(1234)
