from Domain.rezervare import creeaza_rezervare, get_nume, get_clasa
from Logic.clasa_superioara import clasa_superioara_pentru_nume
from Logic.undo_redo import do_undo, do_redo
from Tests.test_crud import get_data


def test_clasa_superioara_pentru_nume():
    rezervari = get_data()
    undo_list = []
    redo_list = []
    rez = creeaza_rezervare(12, 'aero76', 'economy', 3500, 'nu')
    rezervari.append(rez)
    rezervari = clasa_superioara_pentru_nume(rezervari, 'aero76', undo_list, redo_list)
    for rezervare in rezervari:
        if get_nume(rezervare) == 'aero76':
            assert get_clasa(rezervare) == 'economy plus'
    rezervari = do_undo(undo_list, redo_list, rezervari)
    for rezervare in rezervari:
        if get_nume(rezervare) == 'aero76':
            assert get_clasa(rezervare) == 'economy'
    rezervari = do_redo(undo_list, redo_list, rezervari)
    for rezervare in rezervari:
        if get_nume(rezervare) == 'aero76':
            assert get_clasa(rezervare) == 'economy plus'
    rez2 = creeaza_rezervare(13, 'aero55', 'business', 3000, 'da')
    rezervari.append(rez2)
    rezervari = clasa_superioara_pentru_nume(rezervari, 'aero55', undo_list, redo_list)
    for rezervare in rezervari:
        if get_nume(rezervare) == 'aero55':
            assert get_clasa(rezervare) == 'business'
    rezervari = do_undo(undo_list, redo_list, rezervari)
    for rezervare in rezervari:
        if get_nume(rezervare) == 'aero55':
            assert get_clasa(rezervare) == 'business'
    rezervari = do_redo(undo_list, redo_list, rezervari)
    for rezervare in rezervari:
        if get_nume(rezervare) == 'aero55':
            assert get_clasa(rezervare) == 'business'
