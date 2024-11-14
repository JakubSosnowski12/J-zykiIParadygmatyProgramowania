def zadanie1(wagi, max_waga):
    for waga in wagi:
        if waga > max_waga:
            raise ValueError(f"Paczka o wadze {waga} przekracza maksymalną dozwoloną wagę kursu ({max_waga}) kg")
    wagi_sorted = sorted(wagi, reverse=True)
    kursy = []
    for waga in wagi_sorted:
        dodano = False
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodano = True
                break
        if not dodano:
            kursy.append([waga])

    return (len(kursy), kursy)

wagi = [10, 15, 7, 8, 5, 20, 10]
max_waga = 25
wynik = zadanie1(wagi, max_waga)
print(f"Liczba kursów: {wynik[0]}")
print("Paczki w każdym kursie:", wynik[1])