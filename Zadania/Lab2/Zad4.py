import numpy as np
from functools import reduce

def dodaj_macierze(macierz1, macierz2):
    if macierz1.shape == macierz2.shape:
        return macierz1 + macierz2
    else:
        raise ValueError("Macierze muszą mieć te same wymiary do dodania")


def mnoz_macierze(macierz1, macierz2):
    if macierz1.shape[1] == macierz2.shape[0]:
        return np.dot(macierz1, macierz2)
    else:
        raise ValueError(
            "Liczba kolumn w pierwszej macierzy musi być równa liczbie wierszy w drugiej macierzy do mnożenia")


def wykonaj_operacje(operacja, lista_macierzy):
    if operacja == 'dodawanie':
        return reduce(dodaj_macierze, lista_macierzy)
    elif operacja == 'mnozenie':
        return reduce(mnoz_macierze, lista_macierzy)
    else:
        raise ValueError("Brak takiej operacji")


def main():
    macierz1 = np.array([[1, 2], [3, 4]])
    macierz2 = np.array([[5, 6], [7, 8]])
    macierz3 = np.array([[9, 10], [11, 12]])

    lista_macierzy = [macierz1, macierz2, macierz3]

    operacja = input("Wybierz operację (dodawanie/mnozenie): ").lower()

    try:
        wynik = wykonaj_operacje(operacja, lista_macierzy)
        print(f'Wynik operacji {operacja}:\n{wynik}')
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    main()