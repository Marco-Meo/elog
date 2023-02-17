# Erstelle ein Skript, welche einen E-Mail-Text dynamisch erstellt anhand der Eingababeabfrage des Namens.
# Der E-Mail Text ist als Vorlage vorhanden
# Name und Vorname werden als prompt abgefragt.


def create_mail_text() -> str:
    kunden_name = input("Bitte geben Sie Vor-und Nachname ein: (default Max Muster) ") or "Max Muster"
    text_vorlage = """
        Hallo %(name)s

        Herzlich Willkommen bei unserem Newsletter!
        Wir freuen uns dir wöchentlich updates über unsere Produkte und Dienstleistungen mitzuteilen.

        Dein News-Team
        """ % {'name': kunden_name}
    return text_vorlage


if __name__ == '__main__':
    mail_text = create_mail_text()
    print(mail_text)
