# Beispiel für das Lesen und Schreiben von Dateien
import datetime
import os
DATEINAME = r"\\servername\testdateien\datei_1.txt"

def read_file(filepath):
    with open(filepath, 'r') as file:
        print(file.read())


def write_file(filepath, text):
    with open(filepath, 'w', encoding='UTF-8') as file:
        file.write(text)


if __name__ == '__main__':
    text_to_file = input("Bitte Text eingeben: ")
    try:
        # dateipfad = os.path.join(os.getcwd(), 'testdateien', 'datei_3.txt')
        dateiname = f"beispiel.txt"
        heute = datetime.datetime.now()

        dateipfad = os.path.join(
            os.path.dirname(__file__),
            'testdateien',
            str(heute.year),
            str(heute.month),
            str(heute.day),
            dateiname
        )
        if not os.path.exists(dateipfad):
            os.makedirs(os.path.dirname(dateipfad))
        write_file(dateipfad, text_to_file)
    except Exception as e:
        print(e)

    # Datei zum löschen
    dateipfad_del = "testdateien/datei_3.txt"
    try:
        os.remove(dateipfad_del)
    except FileNotFoundError:
        print("Datei nicht gefunden")