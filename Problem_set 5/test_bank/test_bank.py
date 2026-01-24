from bank import value


def test_hello_lower():
    assert value("hello") == 0

def test_hello_uppercase():
    assert value("HELLO") == 0

def test_hello_mixedcase():
    assert value("HeLLo there") == 0

def test_h_only_lower():
    assert value("hi") == 20

def test_h_only_uppercase():
    assert value("HEY") == 20

def test_h_only_mixedcase():
    assert value("hEy there") == 20

def test_non_h_greeting():
    assert value("good morning") == 100

def test_non_h_greeting_uppercase():
    assert value("BYE") == 100
