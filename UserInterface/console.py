from Domain.rezervare import get_str, creeaza_rezervare
from Logic.clasa_superioara import clasa_superioara_pentru_nume
from Logic.crud import create, update, delete
from Logic.ieftinire_procentaj import ieftinire_procentaj_pentru_checkin
from Logic.pret_maxim_pe_clasa import pret_maxim_per_clasa


def show_menu():
    print('1.CRUD')
    print('2.TRECEREA LA O CLASA SUPERIOARA')
    print('3.IEFTINIRE CU UN PROCENTAJ')
    print('4.PRET MAXIM PENTRU FIECARE CLASA')
    print('x.IESIRE')


def handle_add(rezervari):
    try:
        id_rezervare = int(input("Dati id-ul rezervarii "))
        nume = input("Dati numele zborului ")
        clasa = input("Dati clasa zborului: economy, economy plus ori business ")
        pret = float(input("Dati pretul zborului "))
        checkin = input("Dati checkin-ul: da/nu ")
        return create(rezervari, id_rezervare, nume, clasa, pret, checkin)
    except ValueError as ve:
        print('Eroare: ', ve)

    return rezervari


def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))


def handle_update(rezervari):
    try:
        id_rezervare = int(input("Dati id-ul rezervarii care se actualizeaza "))
        nume = input("Dati noul nume al zborului ")
        clasa = input("Dati noua clasa a zborului: economy, economy plus ori business ")
        pret = float(input("Dati noul pret al zborului "))
        checkin = input("Dati noul checkin: da/nu ")
        return update(rezervari, creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin))
    except ValueError as ve:
        print('Eroare: ', ve)
    return rezervari


def handle_delete(rezervari):
    try:
        id_rezervare = int(input("Dati id-ul rezervarii care se va sterge "))
        print("Stergerea a fost efectuata cu succes.")
        return delete(rezervari, id_rezervare)
    except ValueError as ve:
        print('Eroare: ', ve)


def handle_crud(rezervari):
    while True:
        print("1.ADAUGARE")
        print("2.MODIFICARE")
        print("3.STERGERE")
        print("a.AFISARE")
        print("b.REVENIRE")
        optiune = input("Alegeti optiunea dorita ")
        if optiune == '1':
            rezervari = handle_add(rezervari)
        elif optiune == '2':
            rezervari = handle_update(rezervari)
        elif optiune == '3':
            rezervari = handle_delete(rezervari)
        elif optiune == 'a':
            handle_show_all(rezervari)
        elif optiune == 'b':
            break
        else:
            print("Optiune invalida.")
    return rezervari


def handle_clasa_superioara(rezervari):
    try:
        nume1 = input('Dati numele pentru care vreti sa efectuati modificarea: ')
        return clasa_superioara_pentru_nume(rezervari, nume1)
    except ValueError as ve:
        print('Eroare: ', ve)
    return rezervari


def handle_ieftinire_procentaj(rezervari):
    try:
        procentaj = int(input('Dati procentajul cu care vreti sa se efectueze ieftinirea (0-100): '))
        return ieftinire_procentaj_pentru_checkin(rezervari, procentaj)
    except ValueError as ve:
        print('Eroare: ', ve)
    return rezervari


def handle_pret_maxim_pe_clasa(rezervari):
    result = pret_maxim_per_clasa(rezervari)
    for clasa in result:
        print(f'{clasa}: Pretul maxim este {result[clasa]}')


def run_ui(rezervari):
    while True:
        show_menu()
        optiune = input("Alegeti optiunea dorita ")
        if optiune == '1':
            rezervari = handle_crud(rezervari)
        elif optiune == '2':
            rezervari = handle_clasa_superioara(rezervari)
        elif optiune == '3':
            rezervari = handle_ieftinire_procentaj(rezervari)
        elif optiune == '4':
            handle_pret_maxim_pe_clasa(rezervari)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida.")
    return rezervari
