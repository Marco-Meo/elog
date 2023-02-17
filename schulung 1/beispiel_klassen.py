# Beispiel für Klassen

class Person:

    def __init__(self, vorname, nachname, geburtsdatum):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.name = " ".join([self.vorname, self.nachname])

    def __str__(self):
        return self.name

    def change_name(self):
        self.name = " ".join([self.vorname, self.nachname])


class Mitarbeiter(Person):
    lohn = 0
    ferienguthaben = 20
    kinder = []

    def __str__(self):
        return f"{self.name}, {self.lohn}"

    def add_kind(self, vorname, nachname, geburtsdatum):
        self.kinder.append(Person(vorname, nachname, geburtsdatum))

    def get_kinder(self):
        for kind in self.kinder:
            print(kind)

    def __del__(self):
        print("Mitarbeiter gelöscht")


if __name__ == '__main__':
    person_a = Mitarbeiter("Marco", "Meo", "05.08.1982")
    person_a.change_name()
    person_a.lohn = 1000000
    print(person_a)
    person_a.add_kind("Lucie", "Meo", "06.03.2017")
    person_a.add_kind("Vita", "Meo", "28.05.2020")
    print("-" * 10)
    print("Kinder")
    print(person_a.get_kinder())
    del person_a
