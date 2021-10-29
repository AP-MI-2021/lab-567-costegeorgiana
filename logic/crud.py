from Domain.rezervare import creeaza_rezervare
from Domain.rezervare import get_id


def create(lst_rezervari, id_rezervare: int, nume, clasa, pret, checkin):
    """
    Creeaza o rezervare.
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii
    :param nume: numele zborului
    :param clasa: clasa zborului
    :param pret: pretul zborului
    :param checkin: checkin
    :return: o rezervare
    """
    if read_rezervari(lst_rezervari, id_rezervare) is not None:
        raise ValueError(f'Exista deja o rezervare cu id-ul {id_rezervare}')

    rezervare = creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
    return lst_rezervari + [rezervare]


def read_rezervari(lst_rezervari, id_rezervare: int = None):
    """
    Citeste o rezervare.
    :param lst_rezervari:lista de rezervari
    :param id_rezervare: id-ul rezervarii
    :return:-rezervarea cu id-ul id_rezervare, daca exista
            -lista cu toate rezervarile, daca id_rezervare=None
            -None daca nu exista o rezervare cu id_rezervare
    """
    if not id_rezervare:
        return lst_rezervari
    rezervare_cu_id = None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id = rezervare
    if rezervare_cu_id:
        return rezervare_cu_id

    return None


def update(lst_rezervari, new_rezervare):
    """
    Actualizeaza o rezervare.
    :param lst_rezervari: lista cu rezervari
    :param new_rezervare: rezervarea actualizata
    :return:o lista cu rezervari actualizata
    """
    if read_rezervari(lst_rezervari, get_id(new_rezervare)) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {get_id(new_rezervare)} pe care sa o actualizam.')

    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)
    return new_rezervari


def delete(lst_rezervari, id_rezervare: int):
    """
    Stergerea unei rezervari dupa id-ul dat.
    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii
    :return: lista de rezervari fara rezervarea cu id-ul id_rezervare
    """
    if read_rezervari(lst_rezervari, id_rezervare) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {id_rezervare} pe care sa o stergem.')
    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_rezervari.append(rezervare)
    return new_rezervari
