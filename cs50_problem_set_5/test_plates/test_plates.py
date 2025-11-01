from plates import is_valid


def test_one():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_two():
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False


def test_three():
    assert is_valid("OUTATIME") == False
    assert is_valid("NRVOUS") == True


def test_four():
    assert is_valid("ECTO88") == True
    assert is_valid("50") == False
