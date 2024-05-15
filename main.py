import sys

# Funkcje

if len(sys.argv) > 1:
    wersja_jezykowa = sys.argv[1]
else:
    wersja_jezykowa = None

if wersja_jezykowa == 'pl':
    hello_tekst = "Podaj wartosc: "
    end_tekst = "Podana wartosc: "
elif wersja_jezykowa == 'en':
    hello_tekst = "Input value: "
    end_tekst = "Value: "
else:
    hello_tekst = "Input: "
    end_tekst = "Output:"


def pobierz_i_wyswietl_tekst(prompt_wejsciowy, tekst_wyjsciowy):
    # pobieramy wartosc z klawiatury
    wartossc_z_klawiatury = input(prompt_wejsciowy)
    # wypisujemy wartosc na ekran
    print(tekst_wyjsciowy, wartossc_z_klawiatury)


pobierz_i_wyswietl_tekst(prompt_wejsciowy=hello_tekst, tekst_wyjsciowy=end_tekst)
