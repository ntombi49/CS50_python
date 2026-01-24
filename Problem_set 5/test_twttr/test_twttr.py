from twttr import shorten

def test_assert():
    assert shorten("twitter") == "twttr"
    #empty string
    assert shorten("") == ""
    #numbers and special characters
    assert shorten("789$#;;") == "789$#;;"
    #all vowels
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    #a sentence
    assert shorten("The girl is short") == "Th grl s shrt"
