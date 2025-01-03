def paczkipodzial(wagi, maks_waga):
    kursy = []
    obecny_kurs = []
    obecna_waga = 0

    for waga in wagi:
        if obecna_waga + waga <= maks_waga:
            obecny_kurs.append(waga)
            obecna_waga += waga
        else:
            kursy.append(obecny_kurs)
            obecny_kurs = [waga]
            obecna_waga = waga

    if obecny_kurs:
        kursy.append(obecny_kurs)

    return len(kursy), kursy

wagi = [10, 20, 30, 40, 50, 15]
maks_waga = 50
liczba_kursow, kursy = paczkipodzial(wagi, maks_waga)
print("Minimalna liczba kursów:", liczba_kursow)
print("Kursy:", kursy)