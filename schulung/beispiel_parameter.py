from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.description = "Skript zur Archivierung alter Dateien"
    parser.add_argument("-f", "--filter", dest="filter_name")
    args = parser.parse_args()
    print(args.filter_name)
