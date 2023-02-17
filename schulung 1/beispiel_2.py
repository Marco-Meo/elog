# Beispiel für Funktionen

def text_ausgabe():
    """

    :return:
    """
    print("Hello World!")


def text_zusammenfuehren(text_1: str, text_2: str) -> str:
    """
    Setzt den Text zusammen aus den beiden Variablen text_1 und text_2
    :param text_1:
    :param text_2:
    :return: Liefert den Text vom Typ str
    """
    return text_1 + text_2

def text_n_zusammenfuehren(*args):
    """
    Dynamische zusammenführung der Texte
    :param args:
    :return:
    """
    print(args)
    return " ".join([*args])

def funktion_mit_variablen(var_a, var_b = 1, *args, **kwargs):
    print("Variable A: ", var_a)
    print("Variable B: ", var_b)
    print("Argumente:", args)
    print("Key Word Argumente: ", kwargs)



if __name__ == '__main__':
    # text = text_zusammenfuehren("hallo ", "welt")
    # text = text_n_zusammenfuehren("hallo", "welt", "dfasdkj", "sdkd")
    # funktion_mit_variablen("A", "B", "C", "D", E="E", F="F")
    a = lambda x: x * x
    print(a(10))
    #print(text)