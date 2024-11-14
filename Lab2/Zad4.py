from functools import reduce
import numpy as np

def suma_macierzy(macierz1, macierz2):
    return macierz1 + macierz2

def mnozenie_macierzy(macierz1, macierz2):
    return macierz1 * macierz2

macierze = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]), np.array([[9, 10], [11, 12]])]
wynik = reduce(suma_macierzy, macierze)
print("Wynik sumy macierzy:", wynik)
wynik_mnozenia = reduce(mnozenie_macierzy, macierze)
print("Wynik mnożenia macierzy:", wynik_mnozenia)
