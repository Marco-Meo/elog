from ..Aufgaben.aufgabe_2 import entferne_zahlen, entferne_zahlen_aus_text

def test_entferne_zahlen_aus_text():
    assert entferne_zahlen_aus_text("abc 3 der2") == "abc der2"


def test_entferne_zahlen():
    assert entferne_zahlen("abc2") == "abc"
