from Domain.rezervare import get_str, creeaza_rezervare
from Logic.clasa_superioara import clasa_superioara_pentru_nume
from Logic.crud import create, update, delete
from Logic.ieftinire_procentaj import ieftinire_procentaj_pentru_checkin
from Logic.ordonare_descrescator import get_ordonare_descrescator_dupa_pret
from Logic.pret_maxim_pe_clasa import pret_maxim_per_clasa
from Logic.sume_pret_pe_nume import sume_preturi_pentru_nume
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1.CRUD')
    print('2.TRECEREA LA O CLASA SUPERIOARA')
    print('3.IEFTINIRE CU UN PROCENTAJ')
    print('4.PRET MAXIM PENTRU FIECARE CLASA')
    print('5.ORDONARE DESCRESCATOARE DUPA PRET')
    print('6.AFISAREA SUMELOR PRETURILOR PENTRU FIECARE NUME.')
    print('u. UNDO')
    print('r. REDO')
    print('x.IESIRE')


def handle_add(rezervari, undo_list, redo_list):
    try:
        id_rezervare = int(input("Dati id-ul rezervarii "))
        nume = input("Dati numele zborului ")
        clasa = input("Dati clasa zborului: economy, economy plus ori business ")
        pret = float(input("Dati pretul zborului "))
        checkin = input("Dati checkin-ul: da/nu ")
        return create(rezervari, id_rezervare, nume, clasa, pret, checkin, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare: ', ve)

    return rezervari


def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))


def handle_update(rezervari, undo_list, redo_list):
    try:
        id_rezervare = int(input("Dati id-ul rezervarii care se actualizeaza "))
        nume = input("Dati noul nume al zborului ")
        clasa = input("Dati noua clasa a zborului: economy, economy plus ori business ")
        pret = float(input("Dati noul pret al zborului "))
        checkin = input("Dati noul checkin: da/nu ")
        return update(rezervari, creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin), undo_list, redo_list)
    except ValueError as ve:
        print('Eroare: ', ve)
    return rezervari


def handle_delete(rezervari, undo_list, redo_list):
    try:
        id_rezervare = int(input("Dati id-ul rezervarii care se va sterge "))
        print("Stergerea a fost efectuata cu succes.")
        return delete(rezervari, id_rezervare, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare: ', ve)


def handle_crud(rezervari, undo_list, redo_list):
    while True:
        print("1.ADAUGARE")
        print("2.MODIFICARE")
        print("3.STERGERE")
        print("a.AFISARE")
        print("b.REVENIRE")
        optiune = input("Alegeti optiunea dorita ")
        if optiune == '1':
            rezervari = handle_add(rezervari, undo_list, redo_list)
        elif optiune == '2':
            rezervari = handle_update(rezervari, undo_list, redo_list)
        elif optiune == '3':
            rezervari = handle_delete(rezervari, undo_list, redo_list)
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


def handle_ordonare_descrescator(rezervari):
    ordonate = get_ordonare_descrescator_dupa_pret(rezervari)
    handle_show_all(ordonate)


def handle_sume_pret_pe_nume(rezervari):
    result = sume_preturi_pentru_nume(rezervari)
    for nume in result:
        print(f'{nume}: {result[nume]}')


def handle_undo(rezervari, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, rezervari)
    if undo_result is not None:
        return undo_result
    return rezervari


def handle_redo(rezervari, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, rezervari)
    if redo_result is not None:
        return redo_result
    return rezervari


def run_ui(rezervari, undo_list, redo_list):
    while True:
        handle_show_all(rezervari)
        show_menu()
        optiune = input("Alegeti optiunea dorita ")
        if optiune == '1':
            rezervari = handle_crud(rezervari, undo_list, redo_list)
        elif optiune == '2':
            rezervari = handle_clasa_superioara(rezervari)
        elif optiune == '3':
            rezervari = handle_ieftinire_procentaj(rezervari)
        elif optiune == '4':
            handle_pret_maxim_pe_clasa(rezervari)
        elif optiune == '5':
            handle_ordonare_descrescator(rezervari)
        elif optiune == '6':
            handle_sume_pret_pe_nume(rezervari)
        elif optiune == 'u':
            rezervari = handle_undo(rezervari, undo_list, redo_list)
        elif optiune == 'r':
            rezervari = handle_redo(rezervari, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida.")
    return rezervari
