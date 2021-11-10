from Domain.rezervare import creeaza_rezervare, get_pret
from Logic.ieftinire_procentaj import ieftinire_procentaj_pentru_checkin
from Logic.undo_redo import do_undo, do_redo


def test_ieftinire_procentaj_pentru_checkin():
    rezervari = []
    undo_list = []
    redo_list = []
    rez = creeaza_rezervare(12, 'aero76', 'economy', 3500, 'da')
    rez2 = creeaza_rezervare(13, 'aero76', 'economy plus', 4500, 'nu')
    rezervari.append(rez)
    rezervari.append(rez2)
    rezervari = ieftinire_procentaj_pentru_checkin(rezervari, 10, undo_list, redo_list)
    assert get_pret(rezervari[0]) == 3150
    assert get_pret(rezervari[1]) == 4500
    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert get_pret(rezervari[0]) == 3500
    assert get_pret(rezervari[1]) == 4500
    rezervari = do_redo(undo_list, redo_list, rezervari)
    assert get_pret(rezervari[0]) == 3150
    assert get_pret(rezervari[1]) == 4500
    assert do_redo(undo_list, redo_list, rezervari) is None
