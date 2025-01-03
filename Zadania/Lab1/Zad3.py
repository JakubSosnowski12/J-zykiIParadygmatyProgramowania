def optymalizacjaproceduralna(zadania):
    zadania.sort(key=lambda x: x[0])
    calkowity_czas = 0
    czas_oczekiwania = 0

    for czas, nagroda in zadania:
        calkowity_czas += czas
        czas_oczekiwania += calkowity_czas

    return zadania, czas_oczekiwania

def optymalizacjafunkcyjna(zadania):
    posortowane = sorted(zadania, key=lambda x: x[0])
    czas_oczekiwania = sum((i + 1) * zadanie[0] for i, zadanie in enumerate(posortowane))
    return posortowane, czas_oczekiwania

zadania = [(3, 10), (2, 5), (1, 2)]
opt_kolejnosc, czas = optymalizacjaproceduralna(zadania)
print("Kolejność zadań (proceduralnie):", opt_kolejnosc)
print("Czas oczekiwania:", czas)

opt_kolejnosc, czas = optymalizacjafunkcyjna(zadania)
print("Kolejność zadań (funkcyjnie):", opt_kolejnosc)
print("Czas oczekiwania:", czas)