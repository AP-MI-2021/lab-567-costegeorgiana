from Domain.rezervare import creeaza_rezervare
from Logic.clasa_superioara import clasa_superioara_pentru_nume
from Tests.test_crud import get_data


def test_clasa_superioara_pentru_nume():
    rezervari = get_data()
    rez = creeaza_rezervare(12, 'aero76', 'economy', 3500, 'nu')
    rezervari.append(rez)
    updated = clasa_superioara_pentru_nume(rezervari, 'aero76')
    assert rez in rezervari
    assert rez not in updated
    assert len(updated) == len(rezervari)
    rez2 = creeaza_rezervare(13, 'aero55', 'business', 3000, 'da')
    rezervari.append(rez2)
    updated = clasa_superioara_pentru_nume(rezervari, 'aero55')
    assert rez2 in rezervari
    assert rez2 in updated
    assert len(updated) == len(rezervari)