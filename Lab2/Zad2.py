import numpy as np


def walidacja_dodawania(macierz1, macierz2):
    return macierz1.shape == macierz2.shape


def walidacja_mnozenia(macierz1, macierz2):
    return macierz1.shape[1] == macierz2.shape[0]


def wykonaj_operacje(macierz1, macierz2=None, operacja="dodawanie"):
    if operacja == "dodawanie" and macierz2 is not None:
        if walidacja_dodawania(macierz1, macierz2):
            return macierz1 + macierz2
        else:
            raise ValueError("Macierze mają niezgodne wymiary do dodawania.")

    elif operacja == "mnozenie" and macierz2 is not None:
        if walidacja_mnozenia(macierz1, macierz2):
            return macierz1 @ macierz2
        else:
            raise ValueError("Macierze mają niezgodne wymiary do mnożenia.")

    elif operacja == "transponowanie":
        return macierz1.T
    else:
        raise ValueError("Nieznana operacja lub brak wymaganych macierzy.")



macierz_a = np.array([[1, 2], [3, 4]])
macierz_b = np.array([[5, 6], [7, 8]])

print("Dodawanie:")
print(wykonaj_operacje(macierz_a, macierz_b, "dodawanie"))
print("Mnożenie:")
print(wykonaj_operacje(macierz_a, macierz_b, "mnozenie"))
print("Transponowanie:")
print(wykonaj_operacje(macierz_a, operacja="transponowanie"))
