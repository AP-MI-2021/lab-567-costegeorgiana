def creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin):
    """
    Creeaza o rezervare a unei companii aeriene.
    :param id_rezervare: id-ul rezervarii, care este unic
    :param nume: numele zborului
    :param clasa: clasa, economy, economy plus, business
    :param pret: pretul zborului
    :param checkin: da/nu
    :return: o rezervare
    """
    return {
        'id': id_rezervare,
        'nume': nume,
        'clasa': clasa,
        'pret': pret,
        'checkin': checkin,

    }


def get_id(rezervare):
    """
    Getter pentru id-ul rezervarii.
    :param rezervare: rezervarea
    :return: id-ul rezervarii date ca parametru
    """
    return rezervare['id']


def get_nume(rezervare):
    """
    Getter pentru nume.
    :param rezervare: rezervarea
    :return: numele zborului pentru rezervarea data ca parametru
    """
    return rezervare['nume']


def get_clasa(rezervare):
    """
    Getter pentru clasa zborului.
    :param rezervare: rezervarea
    :return: clasa zborului pentru rezervarea data ca parametru
    """
    return rezervare['clasa']


def get_pret(rezervare):
    """
    Getter pentru pretul zborului.
    :param rezervare: rezervarea
    :return: pretul zborului pentru rezervarea data ca parametru.
    """
    return rezervare['pret']


def get_checkin(rezervare):
    """
    Getter pentru checkin.
    :param rezervare: rezervarea
    :return: checkin-ul rezervarii date ca parametru
    """
    return rezervare['checkin']


def get_str(rezervare):
    return f'Rezervarea cu id-ul {get_id(rezervare)}, cu numele de {get_nume(rezervare)},' \
           f' clasa {get_clasa(rezervare)}, pretul {get_pret(rezervare)}, checkin {get_checkin(rezervare)}'
