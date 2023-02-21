import time


def logging_time(func):
    """
    Decorator der die Ausführungszeit misst
    :param func:
    :return:
    """

    def logger(*args, **kwargs):
        print("Start Programm")
        start = time.time()
        func(*args, **kwargs)
        print(f"Ausführungszeit für die Funktion {func.__name__}: {time.time() - start:.5f}s")

    return logger


@logging_time
def calculate_sum(wert: int = 10_000_000):
    summe = sum(range(wert))
    print(f"Summe aller Zahlen zwischen 1 und {wert:_.0f} ist gleich {summe:_.0f}")


if __name__ == '__main__':
    calculate_sum(100_000_000)
