# Übermittle mehrere Dateien auf einen FTP Server
# Konfiguriert wird dies in einer separaten Konfigurationsdatei

import configparser
import ftplib
import os


def load_config(config_file: str = 'config.ini'):
    """
    Lade Konfigurationsdatei und gib Config Objekt zurück
    :param config_file:
    :return:
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def read_file_list(path: str):
    # return [os.path.join(path, f.name) for f in os.scandir(path) if f.is_file()]
    liste_mit_gefundenen_dateien = []
    for gefundener_eintrag_in_ordner in os.scandir(path=path):
        if gefundener_eintrag_in_ordner.is_file():
            datei_mit_pfad = os.path.join(path, gefundener_eintrag_in_ordner.name)
            liste_mit_gefundenen_dateien.append(datei_mit_pfad)
    return liste_mit_gefundenen_dateien


def send_files_to_ftp(files: list[str], server: str, user: str, pwd: str, path: str):
    with ftplib.FTP_TLS(host=server) as ftps:
        ftps.login(user=user, passwd=pwd)
        ftps.cwd(path)
        for file in files:
            try:
                with open(file, 'rb') as open_file:
                    ftps.storbinary(f'STOR {os.path.basename(file)}', open_file)
            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    config = load_config()
    file_list = read_file_list(config.get('Quelle', 'pfad'))

    send_files_to_ftp(
        file_list,
        config.get('FTP', 'server'),
        config.get('FTP', 'user'),
        config.get('FTP', 'pwd'),
        config.get('FTP', 'ftp_path'),
    )
