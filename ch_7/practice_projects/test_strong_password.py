# Pytest unit test for strong_password

from strong_password import strong_password

def test_strong_password():
    """Returns whether a passowrd is considered a strong password based off:
    - Contains at least 8 characters
    - Contains at least one lowercase letter
    - Contains at least one uppercase letter
    - Contains at least one number
    """
    assert strong_password('AbCdE2') == False
    assert strong_password('12345abc') == False
    assert strong_password('PASSWORD1') == False
    assert strong_password('6SEzCrG') == False
    assert strong_password('PwDSIHzuaX') == False

    assert strong_password('AbCdE2df') == True
    assert strong_password('123D45abc') == True
    assert strong_password('Strongpassword123') == True
    assert strong_password('Np!e^E26hF') == True
    assert strong_password('QuYMe2fpdR') == True