def gerade_zahlen(von: int = 1, bis: int = 100) -> list:
    """
    Gibt eine Liste von Geraden Zahlen zwischen den
    :return:
    """
    return [x for x in range(von, bis) if x % 2 == 0]


def gerade_zahlen_2():
    zahlen_liste = []
    for zahl in range(1,100):
        if zahl%2 == 0:
            zahlen_liste.append(zahl)
    return zahlen_liste

if __name__ == '__main__':
    print(gerade_zahlen())
    print(gerade_zahlen_2())
