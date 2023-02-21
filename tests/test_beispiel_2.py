import pytest
from ..schulung.beispiel_2 import text_zusammenfuehren, text_n_zusammenfuehren

def test_text_zusammenfuehren():
    assert text_zusammenfuehren("ab", "cd") == "abcd"
    assert text_zusammenfuehren("abc", "d") != "abc"

def test_text_n_zusammenfuehren():
    assert text_n_zusammenfuehren("hallo", "welt") == "hallo welt"