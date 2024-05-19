SRODOWISKO = 'prod'  # dev / prod

# wartosc_tekstowa = input("Podaj tekst: ")
# wartosc_pola = pole_prostokata(a=10, b=2)
# print("Wyliczona wartosc:", wartosc_pola)


def pole_prostokata(a, b):
    pole = a * b
    return pole


def pobierz_liste_pracownikow(test=False):
    lista_pracownikow = []
    while True:
        czy_dalej = input("Aby kontynuowac wpisz y, aby przerwac wpisz n: ")
        if czy_dalej == 'n':
            break
        imie_nazwisko = input("Podaj imie i nazwisko: ")
        stanowisko = input("Podaj stanowisko: ")
        nowy_pracownik = {'imie_nazwisko': imie_nazwisko, 'stanowisko': stanowisko}
        lista_pracownikow.append(nowy_pracownik)
        if test:
            print("Pobrano:", nowy_pracownik)
    return lista_pracownikow


def pobierz_testowa_liste_pracownikow():
    return [
        {'imie_nazwisko': 'Adam Nowak', 'stanowisko': 'programista'},
        {'imie_nazwisko': 'Kacper Kacper', 'stanowisko': 'programista'},
        {'imie_nazwisko': 'Anon Bimbo', 'stanowisko': 'Sprzedawca'},
        {'imie_nazwisko': 'Anna Kowalska', 'stanowisko': 'IT Director'},
    ]


def pracownicy_po_stanowisku(nazwa_stanowiska, lista_pracownikow):
    lista_pracownikow_na_stanowisku = []
    for pracownik in lista_pracownikow:
        if pracownik['stanowisko'] == nazwa_stanowiska:
            lista_pracownikow_na_stanowisku.append(pracownik)
    return lista_pracownikow_na_stanowisku, len(lista_pracownikow_na_stanowisku)


if SRODOWISKO == 'dev':
    lista_pracownikow = pobierz_testowa_liste_pracownikow()
elif SRODOWISKO == 'prod':
    lista_pracownikow = pobierz_liste_pracownikow()
else:
    print("WARNING: nieznane srodowisko")
    lista_pracownikow = []

# Zadanie:  wypisz tylko programistow
programisci, liczba_programistow = pracownicy_po_stanowisku(lista_pracownikow=lista_pracownikow, nazwa_stanowiska='programista')
print(f"Mamy {liczba_programistow} programistow")
print("Programisci:", programisci)

dyrektorzy, liczba_dyrektorow = pracownicy_po_stanowisku('IT Director', lista_pracownikow=lista_pracownikow)
print(f"Mamy {liczba_dyrektorow} dyrektorow")
print("Dyrektorzy:", dyrektorzy)
