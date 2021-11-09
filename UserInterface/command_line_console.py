from Domain.rezervare import get_str
from Logic.crud import create, delete
from Logic.ordonare_descrescator import get_ordonare_descrescator_dupa_pret
from UserInterface.console import handle_show_all


def show_new_menu():
    print("INTRODUCETI OPTIUNILE CU ';' INTRE ELE.")
    print("add - ADAUGAREA UNEI REZERVARI./"
          "(Exemplu: add : id, nume, clasa(economy/ economy plus/ business), pret, checkin;)")
    print("showall - AFISAREA LISTE DE REZERVARI. (Exemplu: showall;)")
    print("delete - STERGEREA UNEI REZERVARI. (Exemplu: delete : id;)")
    print("ordonare - ORDONAREA REZERVARILOR DESCRESCATOR DUPA PRET. (Exemplu: ordonare;)")
    print("iesire - IESIRE DIN PROGRAM. (Exemplu: iesire;)")


def handle_new_add(rezervari, rezervare):
    try:
        if ',' in rezervare:
            rezervare_split = rezervare.split(',')
            id_rezervare = int(rezervare_split[0])
            nume = rezervare_split[1]
            clasa = rezervare_split[2]
            pret = float(rezervare_split[3])
            if rezervare_split[4] == ' da' or rezervare_split[4] == ' nu':
                checkin = rezervare_split[4]
                return create(rezervari, id_rezervare, nume, clasa, pret, checkin, [], [])
        else:
            print('Eroare:', TypeError(f'Trebuie pus "," dupa fiecare camp.'))
    except ValueError as ve:
        print('Eroare: ', ve)
    return rezervari


def handle_new_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))


def handle_new_delete(rezervari, id_rez: int):
    try:
        id_rezervare = id_rez
        print("Stergerea a fost efectuata cu succes.")
        return delete(rezervari, id_rezervare, [], [])
    except ValueError as ve:
        print('Eroare: ', ve)


def handle_ordonare(rezervari):
    ordonate = get_ordonare_descrescator_dupa_pret(rezervari)
    handle_show_all(ordonate)


def run_ui_line_console(rezervari):
    while True:
        show_new_menu()
        opt = str(input("Dati comenzile: "))
        opt_split = opt.split(';')
        for comm in opt_split:
            nr = 0
            if 'add' in comm:
                if nr == 0:
                    nr += 1
                    if ':' in comm:
                        comm_split = comm.split(':')
                        rezervari = handle_new_add(rezervari, comm_split[1])
                    else:
                        print('Eroare:', TypeError(f'Trebuie pus ":" dupa add.'))
                else:
                    print('Eroare:', TypeError(f'Trebuie pus ";" dupa fiecare optiune.'))

            if 'showall' in comm:
                if nr == 0:
                    nr += 1
                    handle_new_show_all(rezervari)
                else:
                    print('Eroare:', TypeError(f'Trebuie pus ";" dupa fiecare optiune.'))
            if 'delete' in comm:
                if nr == 0:
                    nr += 1
                    if ':' in comm:
                        comm_del_split = comm.split(':')
                        rezervari = handle_new_delete(rezervari, int(comm_del_split[1]))
                    else:
                        print('Eroare:', TypeError(f'Trebuie pus ":" dupa delete.'))
                else:
                    print('Eroare:', TypeError(f'Trebuie pus ";" dupa fiecare optiune.'))
            if 'ordonare' in comm:
                handle_ordonare(rezervari)
        if 'iesire' in opt_split:
            break
