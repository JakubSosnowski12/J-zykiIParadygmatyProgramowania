przedmioty = [
    {"waga": 2, "wartosc": 3},
    {"waga": 3, "wartosc": 4},
    {"waga": 4, "wartosc": 5},
    {"waga": 5, "wartosc": 8}
]
pojemnosc = 5
dp = [[0] * (pojemnosc + 1) for _ in range(len(przedmioty) + 1)]

