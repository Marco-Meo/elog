import datetime
import ftplib
import os
import ssl
import logging
import shutil
import configparser
import logging.config

logging.config.fileConfig('logger.ini')
logger = logging.getLogger('ftpTest')

def load_config(config_file='config.ini'):
    """
    Funktion zum Lesen der Konfigurationsdatei
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def submit_mutible_files_to_ftp():
    pass


def send_file_to_ftp(dateipfad, server, user, pwd, ftp_path):

    if not os.path.exists(dateipfad):
        raise Exception(f"Datei {dateipfad} exisitiert nicht!")

    with ftplib.FTP_TLS() as ftps:
        ftps.ssl_version = ssl.PROTOCOL_TLS
        logger.info(ftps.connect(host=server, port=21, timeout=3))
        logger.info(ftps.set_pasv(True))
        logger.info(ftps.login(user=user, passwd=pwd))
        # logger.info(ftps.prot_p())
        ftps.cwd(ftp_path)
        with open(dateipfad, 'rb') as file:
            logger.info(f"Übermittle Datei {os.path.basename(dateipfad)} aus Dateipfad {os.path.dirname(dateipfad)}")
            # STOR datei_1.txt
            ftps.storbinary(f"STOR {os.path.basename(dateipfad)}", file)

        # todo: übertragene Datei löschen oder archivieren
        archiv_pfad = os.path.join(os.path.dirname(dateipfad), 'Archiv', os.path.basename(dateipfad))
        if not os.path.exists(archiv_pfad):
            os.makedirs(os.path.dirname(archiv_pfad))
        shutil.move(dateipfad, archiv_pfad)
        dateiliste = ftps.mlsd()
        for datei in dateiliste:
            print(datei)


if __name__ == '__main__':
    logger.info("Starte Programm FTP")
    config = load_config()
    dateipfad = os.path.join(os.path.dirname(__file__), 'testdateien', 'datei_1.txt')
    try:
        send_file_to_ftp(
            dateipfad,
            server=config.get('FTP', 'server'),
            user=config.get('FTP', 'user'),
            pwd=config.get('FTP', 'pwd'),
            ftp_path=config.get('FTP', 'ftp_path')
        )
    except Exception as e:
        logger.error(e)