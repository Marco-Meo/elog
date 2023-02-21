# Beispiele für Logging in Python
import logging
import logging.handlers

logger = logging.getLogger("main")

if __name__ == '__main__':
    # logging.basicConfig(filename="logs/main.log", level=logging.WARNING)
    handler = logging.handlers.TimedRotatingFileHandler(
        'logs/main.log',
        when="midnight",
        interval=1,
        backupCount=10
    )
    frm = logging.Formatter("{asctime} {levelname:8}: {message}", "%d.%m.%Y %H:%M:%S", style="{")
    handler.setFormatter(frm)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info("Programm Start")
    logger.warning("Dies ist eine Warnung")
    logger.error("Dies ist ein Fehler")
