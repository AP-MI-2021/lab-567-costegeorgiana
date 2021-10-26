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
    rezervare = creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)
    return lst_rezervari + [rezervare]


def read_rezervari(lst_rezervari, id_rezervare: int = None):
    """
    Citeste o rezervare.
    :param lst_rezervari:lista de rezervari
    :param id_rezervare: id-ul rezervarii
    :return: rezervarea cu id-ul id_rezervare sau lista cu toate rezervarile, daca id_rezervare=None
    """
    rezervare_cu_id = None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id = rezervare
    if rezervare_cu_id:
        return rezervare_cu_id
    return lst_rezervari


def update(lst_rezervari, new_rezervare):
    """
    Actualizeaza o rezervare.
    :param lst_rezervari: lista cu rezervari
    :param new_rezervare: rezervarea actualizata
    :return:o lista cu rezervari actualizata
    """
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
    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_rezervari.append(rezervare)
    return new_rezervari
