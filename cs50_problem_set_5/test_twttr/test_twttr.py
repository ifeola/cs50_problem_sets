import pytest
from twttr import shorten


def main():
    test_twttr()
    test_numb()


def test_twttr():
    assert shorten("Hello") == "Hll"
    assert shorten("How old are you?") == "Hw ld r y?"
    assert shorten("Introduction") == "ntrdctn"


def test_numb():
    with pytest.raises(TypeError):
        shorten(123)


if __name__ == "__main__":
    main()
