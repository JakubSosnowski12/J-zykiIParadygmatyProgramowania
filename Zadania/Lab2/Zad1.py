import re
from collections import Counter

stop_words = set([
    "i", "a", "the", "to", "of", "in", "on", "for", "with", "at", "by", "an", "this", "that", "is", "was", "were", "are"
])


def analiza_tekstu(tekst):
    akapity = tekst.split('\n')
    liczba_akapitow = len(akapity)

    zdania = re.split(r'[.!?]', tekst)
    liczba_zdan = len([s for s in zdania if s.strip()])

    slowa = re.findall(r'\b\w+\b', tekst.lower())
    liczba_slow = len(slowa)

    print(f'Liczba akapitów: {liczba_akapitow}')
    print(f'Liczba zdań: {liczba_zdan}')
    print(f'Liczba słów: {liczba_slow}')

    return slowa

def najczesciej_wystepujace_slowa(slowa):
    przefiltrowane_slowa = [slowo for slowo in slowa if slowo not in stop_words]

    zliczone_slowa = Counter(przefiltrowane_slowa)

    najczestsze = zliczone_slowa.most_common(10)
    print('Najczęściej występujące słowa (po wykluczeniu stop words):')
    for slowo, liczba in najczestsze:
        print(f'{slowo}: {liczba}')


def transformacja_slow_zaczynajacych_sie_na_a(slowa):
    przeksztalcone_slowa = [
        slowo[::-1] if slowo.startswith('a') or slowo.startswith('A') else slowo
        for slowo in slowa
    ]
    return przeksztalcone_slowa


def main():
    tekst = """
    Ala ma kota, a kot ma Alę i żyć bez siebie nie mogą wcale
    """

    slowa = analiza_tekstu(tekst)
    najczesciej_wystepujace_slowa(slowa)
    przeksztalcone_slowa = transformacja_slow_zaczynajacych_sie_na_a(slowa)

    print("\nPrzekształcone słowa:")
    print(' '.join(przeksztalcone_slowa))

if __name__ == "__main__":
    main()
