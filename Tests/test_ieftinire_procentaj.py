from Domain.rezervare import creeaza_rezervare, get_pret
from Logic.ieftinire_procentaj import ieftinire_procentaj_pentru_checkin


def test_ieftinire_procentaj_pentru_checkin():
    rezervari = []
    rez = creeaza_rezervare(12, 'aero76', 'economy', 3500, 'da')
    rez2 = creeaza_rezervare(13, 'aero76', 'economy plus', 4500, 'nu')
    rezervari.append(rez)
    rezervari.append(rez2)
    new_rez = ieftinire_procentaj_pentru_checkin(rezervari, 10)
    assert get_pret(new_rez[0]) == 3150
    assert get_pret(new_rez[1]) == 4500
