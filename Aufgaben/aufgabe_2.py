def entferne_zahlen(text):
    text2 = []
    zahlen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for t in text:
        if t not in zahlen:
            text2.append(t)
    text2 = "".join(text2)
    return text2



def entferne_zahlen_aus_text(text: str) -> str:
    """
    Funktion, welche die Zahlen aus einem Text entfernt.
    :param text:
    :return:
    """
    text = text.split()
    for wort in text:
        if wort.isdigit():
            text.remove(wort)
    text = " ".join(text)
    return text


if __name__ == '__main__':
    text = "Meine 3 Kinder sind alle älter als 4 Jahre"
    print(entferne_zahlen(text))
    print(entferne_zahlen_aus_text(text))
