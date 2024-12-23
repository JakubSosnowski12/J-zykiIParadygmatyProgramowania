import json

def menu():
    print("\nMenu:")
    print("1. Dodaj książkę")
    print("2. Usuń książkę")
    print("3. Pokaż książki")
    print("4. Wyszukaj książki")
    print("5. Wyjdź")


def zapis_json(lista_ksiazek, nazwa_pliku="ksiazki.json"):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(lista_ksiazek, plik, ensure_ascii=False, indent=4)


def wczytaj_z_json(nazwa_pliku="ksiazki.json"):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return []


def dodaj_ksiazke(lista_ksiazek):
    tytul = input("Podaj tytuł książki: ")
    autor = input("Podaj autora książki: ")
    rok = input("Podaj rok wydania książki: ")
    ksiazka = {"tytul": tytul, "autor": autor, "rok": rok}
    lista_ksiazek.append(ksiazka)
    zapis_json(lista_ksiazek)
    print("Dodano książkę!")


def usun_ksiazke(lista_ksiazek):
    tytul = input("Podaj tytuł książki do usunięcia: ")
    for ksiazka in lista_ksiazek:
        if ksiazka["tytul"].lower() == tytul.lower():
            lista_ksiazek.remove(ksiazka)
            zapis_json(lista_ksiazek)
            print("Książka została usunięta")
            return
    print("Nie znaleziono książki")


def pokaz_ksiazki(lista_ksiazek):
    if not lista_ksiazek:
        print("Lista książek jest pusta")
    else:
        print("\nLista książek:")
        for i, ksiazka in enumerate(lista_ksiazek, 1):
            print(f"{i}. {ksiazka['tytul']} - {ksiazka['autor']} ({ksiazka['rok']})")


def wyszukaj_ksiazke(lista_ksiazek):
    tytul = input("Podaj tytuł książki do wyszukania: ")
    znaleziono = False
    for ksiazka in lista_ksiazek:
        if tytul.lower() in ksiazka["tytul"].lower():
            print(f"Znaleziono: {ksiazka['tytul']} - {ksiazka['autor']} ({ksiazka['rok']})")
            znaleziono = True
    if not znaleziono:
        print("Nie znaleziono tytułu")


def main():
    lista_ksiazek = wczytaj_z_json()
    while True:
        menu()
        wybor = input("Wybierz opcję (1-5): ")
        if wybor == "1":
            dodaj_ksiazke(lista_ksiazek)
        elif wybor == "2":
            usun_ksiazke(lista_ksiazek)
        elif wybor == "3":
            pokaz_ksiazki(lista_ksiazek)
        elif wybor == "4":
            wyszukaj_ksiazke(lista_ksiazek)
        elif wybor == "5":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowa opcja")


if __name__ == "__main__":
    main()
