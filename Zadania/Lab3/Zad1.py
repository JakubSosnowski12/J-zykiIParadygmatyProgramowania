
class Pracownik:
    def __init__(self, imie, wiek, wynagrodzenie):
        self.imie = imie
        self.wiek = wiek
        self.wynagrodzenie = wynagrodzenie

    def __repr__(self):
        return f"Pracownik(Imię: {self.imie}, Wiek: {self.wiek}, Wynagrodzenie: {self.wynagrodzenie})"


class MenedżerPracowników:
    def __init__(self):
        self.pracownicy = []

    def dodaj_pracownika(self, imie, wiek, wynagrodzenie):
        nowy_pracownik = Pracownik(imie, wiek, wynagrodzenie)
        self.pracownicy.append(nowy_pracownik)

    def wyswietl_wszystkich_pracownikow(self):
        if not self.pracownicy:
            print("Brak pracowników w systemie")
        else:
            for pracownik in self.pracownicy:
                print(pracownik)

    def usun_pracownikow_w_przedziale_wieku(self, min_wiek, max_wiek):
        self.pracownicy = [pracownik for pracownik in self.pracownicy if not (min_wiek <= pracownik.wiek <= max_wiek)]

    def znajdz_pracownika_po_imieniu(self, imie):
        for pracownik in self.pracownicy:
            if pracownik.imie.lower() == imie.lower():
                return pracownik
        return None

    def zaktualizuj_wynagrodzenie(self, imie, nowe_wynagrodzenie):
        pracownik = self.znajdz_pracownika_po_imieniu(imie)
        if pracownik:
            pracownik.wynagrodzenie = nowe_wynagrodzenie
            print(f"Wynagrodzenie pracownika {imie} zostało zaktualizowane na {nowe_wynagrodzenie}")
        else:
            print(f"Pracownik o imieniu {imie} nie został znaleziony")

class InterfejsUzytkownika:
    def __init__(self, menedżer_pracowników):
        self.menedżer_pracowników = menedżer_pracowników

    def dodaj_pracownika(self):
        imie = input("Podaj imię pracownika: ")
        wiek = int(input("Podaj wiek pracownika: "))
        wynagrodzenie = float(input("Podaj wynagrodzenie pracownika: "))
        self.menedżer_pracowników.dodaj_pracownika(imie, wiek, wynagrodzenie)

    def wyswietl_pracownikow(self):
        self.menedżer_pracowników.wyswietl_wszystkich_pracownikow()

    def usun_pracownikow(self):
        min_wiek = int(input("Podaj minimalny wiek: "))
        max_wiek = int(input("Podaj maksymalny wiek: "))
        self.menedżer_pracowników.usun_pracownikow_w_przedziale_wieku(min_wiek, max_wiek)

    def zaktualizuj_wynagrodzenie(self):
        imie = input("Podaj imię pracownika: ")
        nowe_wynagrodzenie = float(input("Podaj nowe wynagrodzenie: "))
        self.menedżer_pracowników.zaktualizuj_wynagrodzenie(imie, nowe_wynagrodzenie)


def main():
    menedżer_pracowników = MenedżerPracowników()
    interfejs_uzytkownika = InterfejsUzytkownika(menedżer_pracowników)

    while True:
        print("\nMenu Systemu Pracowników:")
        print("1. Dodaj pracownika")
        print("2. Wyświetl wszystkich pracowników")
        print("3. Usuń pracowników w przedziale wiekowym")
        print("4. Zaktualizuj wynagrodzenie pracownika")
        print("5. Wyjście")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            interfejs_uzytkownika.dodaj_pracownika()
        elif wybor == "2":
            interfejs_uzytkownika.wyswietl_pracownikow()
        elif wybor == "3":
            interfejs_uzytkownika.usun_pracownikow()
        elif wybor == "4":
            interfejs_uzytkownika.zaktualizuj_wynagrodzenie()
        elif wybor == "5":
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie")

if __name__ == "__main__":
    main()
