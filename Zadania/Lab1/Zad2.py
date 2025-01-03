def bfs(graf, start, cel):
    from collections import deque

    kolejka = deque([(start, [start])])
    odwiedzone = []

    while kolejka:
        wierzcholek, sciezka = kolejka.popleft()
        if wierzcholek not in odwiedzone:
            odwiedzone.append(wierzcholek)
            for sasiad in graf[wierzcholek]:
                nowa_sciezka = sciezka + [sasiad]
                if sasiad == cel:
                    return nowa_sciezka
                kolejka.append((sasiad, nowa_sciezka))

    return []
graf = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start, cel = 'A', 'F'
najkrotsza_sciezka = bfs(graf, start, cel)
print("Najkrótsza ścieżka:", najkrotsza_sciezka)