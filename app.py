def pole_prostokata(a, b):
    pole = a * b
    return pole

# wartosc_tekstowa = input("Podaj tekst: ")
# wartosc_pola = pole_prostokata(a=10, b=2)
# print("Wyliczona wartosc:", wartosc_pola)

def pobierz_liste_pracownikow():
    lista_pracownikow = []
    while True:
        czy_dalej = input("Aby kontynuowac wpisz y, aby przerwac wpisz n: ")
        if czy_dalej == 'n':
            break
        imie_nazwisko = input("Podaj imie i nazwisko: ")
        stanowisko = input("Podaj stanowisko: ")
        nowy_pracownik = {'imie_nazwisko': imie_nazwisko, 'stanowisko': stanowisko}
        lista_pracownikow.append(nowy_pracownik)
    return lista_pracownikow

lista_pracownikow = pobierz_liste_pracownikow()
print(lista_pracownikow)




