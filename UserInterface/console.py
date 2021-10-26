from Domain.rezervare import get_str, creeaza_rezervare
from Logic.crud import create, update, delete


def show_menu():
    print('1.CRUD')
    print('2.TRECEREA LA O CLASA SUPERIOARA')
    print('x.IESIRE')


def handle_add(rezervari):
    id_rezervare = int(input("Dati id-ul rezervarii "))
    nume = input("Dati numele zborului ")
    clasa = input("Dati clasa zborului: economy, economy plus ori business ")
    pret = float(input("Dati pretul zborului "))
    checkin = input("Dati checkin-ul: da/nu ")
    return create(rezervari, id_rezervare, nume, clasa, pret, checkin)


def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))


def handle_update(rezervari):
    id_rezervare = int(input("Dati id-ul rezervarii care se actualizeaza "))
    nume = input("Dati noul nume al zborului ")
    clasa = input("Dati noua clasa a zborului: economy, economy plus ori business ")
    pret = float(input("Dati noul pret al zborului "))
    checkin = input("Dati noul checkin: da/nu ")
    return update(rezervari, creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin))


def handle_delete(rezervari):
    id_rezervare = int(input("Dati id-ul rezervarii care se va sterge "))
    print("Stergerea a fost efectuata cu succes.")
    return delete(rezervari, id_rezervare)


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


def run_ui(rezervari):
    while True:
        show_menu()
        optiune = input("Alegeti optiunea dorita ")
        if optiune == '1':
            rezervari = handle_crud(rezervari)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida.")
    return rezervari
