
from plates import is_valid

def test_valid_plate_letters_only():
    assert is_valid("CS50") == True

def test_invalid_too_short():
    assert is_valid("A") == False

def test_invalid_too_long():
    assert is_valid("CS50XYZ") == False

def test_invalid_first_char_number():
    assert is_valid("1CS50") == False

def test_invalid_zero_first_number():
    assert is_valid("CS05") == False

def test_invalid_letter_after_number():
    assert is_valid("CS5A") == False

def test_invalid_symbol():
    assert is_valid("CS-50") == False
