zadania = [
    {"nazwa": "Zadanie1", "czas": 4, "nagroda": 10},
    {"nazwa": "Zadanie2", "czas": 2, "nagroda": 20},
    {"nazwa": "Zadanie3", "czas": 1, "nagroda": 15},
    {"nazwa": "Zadanie4", "czas": 3, "nagroda": 30},
]

def optymalizacja_proceduralna(zadania):
    zadania.sort(key=lambda x: x["czas"])


    czas_oczekiwania = 0
    calkowity_czas_ocz = 0
    zysk = 0
    kolejnosc = []

    for zadanie in zadania:
        kolejnosc.append(zadanie["nazwa"])

        czas_oczekiwania += zadanie["czas"]
        calkowity_czas_ocz += czas_oczekiwania


        zysk += zadanie["nagroda"]


    return kolejnosc, calkowity_czas_ocz, zysk


kolejnosc, calkowity_czas_ocz, zysk = optymalizacja_proceduralna(zadania)
print("Optymalna kolejność zadań:", kolejnosc)
print("Całkowity czas oczekiwania:", calkowity_czas_ocz)
print("Całkowity zysk:", zysk)
