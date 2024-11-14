def dynamiczna_analiza(dane):
    liczby = list(filter(lambda x: isinstance(x, (int, float)), dane))
    max_liczba = max(liczby, default=None)


    napisy = list(filter(lambda x: isinstance(x, str), dane))
    najdluzszy_napis = max(napisy, key=len, default=None)


    krotki = list(filter(lambda x: isinstance(x, tuple), dane))
    najwieksza_krotka = max(krotki, key=len, default=None)

    return {
        "max_liczba": max_liczba,
        "najdluzszy_napis": najdluzszy_napis,
        "najwieksza_krotka": najwieksza_krotka
    }


dane = [123, "hello", (1, 2, 3), 45.67, "world", (4, 5), 999, "Python", (6, 7, 8, 9)]
wynik = dynamiczna_analiza(dane)

print("Największa liczba:", wynik["max_liczba"])
print("Najdłuższy napis:", wynik["najdluzszy_napis"])
print("Krotka o największej liczbie elementów:", wynik["najwieksza_krotka"])
