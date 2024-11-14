from collections import Counter
import re


STOP_WORDS = {"i", "a", "to", "w", "na", "z", "jest", "że", "do", "dla", "jak", "o"}


def analiza_tekstu(tekst):

    akapity = tekst.split("\n\n")
    liczba_akapitow = len([a for a in akapity if a.strip()])


    liczba_zdan = len(re.findall(r"[.!?]", tekst))


    slowa = re.findall(r"\b\w+\b", tekst.lower())
    liczba_slow = len(slowa)


    slowa_bez_stop = [slowo for slowo in slowa if slowo not in STOP_WORDS]
    najczestsze_slowa = Counter(slowa_bez_stop).most_common(5)


    transformed_slowa = [
        slowo[::-1] if slowo.lower().startswith("a") else slowo
        for slowo in slowa
    ]

    return {
        "liczba_slow": liczba_slow,
        "liczba_zdan": liczba_zdan,
        "liczba_akapitow": liczba_akapitow,
        "najczestsze_slowa": najczestsze_slowa,
        "transformed_slowa": transformed_slowa
    }



tekst = """Ala ma kota. Kot jest wesoły i lubi bawić się z Alą.
Ania także ma kota, ale jej kot jest bardziej spokojny.
Wszyscy lubią swoje zwierzęta."""

wynik = analiza_tekstu(tekst)
print("Liczba słów:", wynik["liczba_slow"])
print("Liczba zdań:", wynik["liczba_zdan"])
print("Liczba akapitów:", wynik["liczba_akapitow"])
print("Najczęściej występujące słowa:", wynik["najczestsze_slowa"])
print("Słowa po transformacji:", wynik["transformed_slowa"])
