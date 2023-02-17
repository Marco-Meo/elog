from dataclasses import dataclass

@dataclass
class Person:
    vorname: str
    nachname: str
    geburtsdatum: str

    def change_name(self):
        self.name = " ".join([self.vorname, self.nachname])

@dataclass
class Mitarbeiter(Person):
    lohn = 0
    ferienguthaben = 20
    kinder = []

    def add_kind(self, vorname, nachname, geburtsdatum):
        self.kinder.append(Person(vorname, nachname, geburtsdatum))

    def get_kinder(self):
        for kind in self.kinder:
            print(kind)

    def __del__(self):
        print("Mitarbeiter gelöscht")


if __name__ == '__main__':
    ma_mm = Mitarbeiter(
        vorname="Marco",
        nachname="Meo",
        geburtsdatum="05.08.1982"
    )
    print(ma_mm)