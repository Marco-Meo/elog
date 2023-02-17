import datetime
from datetime import date


def berechnung_jahrgang(alter: int) -> str:
    """
    Berechnung des Jahrgangs anhand des Alters.
    :param alter: Alter als integer
    :return: Jahrgang als String
    """
    if alter < 0:
        raise TypeError("Alter unter 0")
    return datetime.date.today().year - alter


def berechnung_alter(geburtsdatum: str) -> int:
    geburtsdatum = datetime.datetime.strptime(geburtsdatum, "%d.%m.%Y")
    date_diff = datetime.datetime.now() - geburtsdatum
    print(f"Alter in Tage: {date_diff.days}")
    return datetime.datetime.now().year - geburtsdatum.year


if __name__ == '__main__':
    namen = input("Geben Sie Ihren Namen ein: ")
    # alter = input("Geben Sie Ihr Alter in Jahren ein: ")
    geburtsdatum = input("Geben Sie Ihr Geburtsdatum ein (dd.mm.yyyy):")

    print(f"Hallo {namen}")
    try:
        # jahrgang = berechnung_jahrgang(int(alter))
        # print(f"Dein Jahrgang ist {jahrgang}")
        alter = berechnung_alter(geburtsdatum)
        print(f"Du bist {alter} Jahre alt")
    except TypeError:
        print("Type Error")
    except Exception as e:
        print(e)
