# Pytest unit test for valid date

from date_detection import valid_date

def test_valid_date():
    assert valid_date(0, 1, 2000) == False
    assert valid_date(29, 2, 1900) == False
    assert valid_date(29, 2, 2500) == False
    assert valid_date(29, 2, 1999) == False
    assert valid_date(-1, 10, 1234) == False
    assert valid_date(0, 0, 1000) == False

    assert valid_date(1, 1, 2000) == True
    assert valid_date(29, 2, 2020) == True
    assert valid_date(29, 2, 2032) == True
    assert valid_date(29, 2, 1988) == True
    assert valid_date(4, 8, 2952) == True
    assert valid_date(27, 2, 2281) == True
