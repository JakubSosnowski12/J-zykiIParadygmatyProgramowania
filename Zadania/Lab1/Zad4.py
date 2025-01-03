def plecak(przedmioty, pojemnosc):
    n = len(przedmioty)
    dp = [[0 for _ in range(pojemnosc + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        waga, wartosc = przedmioty[i - 1]
        for j in range(pojemnosc + 1):
            if waga <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - waga] + wartosc)
            else:
                dp[i][j] = dp[i - 1][j]

    wynik = []
    w = pojemnosc
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            wynik.append(przedmioty[i - 1])
            w -= przedmioty[i - 1][0]

    return dp[n][pojemnosc], wynik

przedmioty = [(2, 3), (1, 2), (3, 4), (2, 2)]
pojemnosc = 5
maks_wartosc, wybrane = plecak(przedmioty, pojemnosc)
print("Maksymalna wartość (proceduralnie):", maks_wartosc)
print("Wybrane przedmioty:", wybrane)
