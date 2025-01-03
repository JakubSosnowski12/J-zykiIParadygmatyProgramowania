import numpy as np


def kompatybilnosc_dodawania(macierz1, macierz2):
    return macierz1.shape == macierz2.shape


def kompatybilnosc_mnozenia(macierz1, macierz2):
    return macierz1.shape[1] == macierz2.shape[0]


def wykonaj_operacje(operacja_str):
    wynik = None

    try:
        eval(operacja_str)
    except Exception as e:
        print(f"Nie udało się wykonać operacji: {e}")

    return wynik


def main():
    macierz1 = np.array([[1, 2], [3, 4]])
    macierz2 = np.array([[5, 6], [7, 8]])

    operacje = [
        "wynik = macierz1 + macierz2",
        "wynik = macierz1 @ macierz2",
        "wynik = macierz1.T",
    ]

    for operacja in operacje:
        print(f"Operacja: {operacja}")
        if "macierz1 + macierz2" in operacja and kompatybilnosc_dodawania(macierz1, macierz2):
            print("Wykonywanie operacji dodawania")
            wynik = wykonaj_operacje(operacja)
            print(f"Wynik: \n{wynik}")
        elif "macierz1 @ macierz2" in operacja and kompatybilnosc_mnozenia(macierz1, macierz2):
            print("Wykonywanie operacji mnożenia")
            wynik = wykonaj_operacje(operacja)
            print(f"Wynik: \n{wynik}")
        elif "macierz1.T" in operacja:
            print("Wykonywanie operacji transponowania")
            wynik = wykonaj_operacje(operacja)
            print(f"Wynik: \n{wynik}")
        else:
            print("Operacja nie jest kompatybilna")


if __name__ == "__main__":
    main()