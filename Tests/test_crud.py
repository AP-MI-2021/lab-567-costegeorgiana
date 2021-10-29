from Domain.rezervare import creeaza_rezervare, get_id
from Logic.crud import create, read_rezervari, update, delete


def get_data():
    return [
        creeaza_rezervare(1, 'axe12', 'economy', 1000, 'da'),
        creeaza_rezervare(2, 'axe13', 'economy plus', 1600, 'nu'),
        creeaza_rezervare(3, 'axe14', 'economy plus', 1600.60, 'da'),
        creeaza_rezervare(4, 'axe12', 'business', 3000, 'nu'),
        creeaza_rezervare(5, 'axe13', 'economy', 1000.80, 'da'),
    ]


def test_create():
    rezervari = get_data()
    params = (6, 'rino34', 'business', 3000, 'nu')
    r_new = creeaza_rezervare(*params)
    new_rezervari = create(rezervari, *params)
    assert len(new_rezervari) == len(rezervari) + 1
    assert r_new in new_rezervari
    # testam daca se lanseaza exceptie pentru id duplicat
    params2 = (6, 'aero87', 'economy', 2000, 'nu')
    try:
        _ = create(new_rezervari, *params2)
        assert False
    except ValueError:
        assert True


def test_read():
    rezervari = get_data()
    some_rez = rezervari[2]
    assert read_rezervari(rezervari, get_id(some_rez)) == some_rez
    assert read_rezervari(rezervari, None) == rezervari


def test_update():
    rezervari = get_data()
    rez_updated = creeaza_rezervare(2, 'aero76', 'business', 3500, 'nu')
    updated = update(rezervari, rez_updated)
    assert rez_updated in updated
    assert rez_updated not in rezervari
    assert len(updated) == len(rezervari)


def test_delete():
    rezervari = get_data()
    to_delete = 3
    rez_deleted = read_rezervari(rezervari, to_delete)
    deleted = delete(rezervari, to_delete)
    assert rez_deleted not in deleted
    assert rez_deleted in rezervari
    assert len(deleted) == len(rezervari) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
