from Domain.rezervare import get_nume, get_clasa, creeaza_rezervare, get_id, get_pret, get_checkin


def clasa_superioara_pentru_nume(lst_rezervari, nume1, undo_list, redo_list):
    """
    Trecerea la o clasa superioara pentru rezervarile facute pe un nume citit de la tastatura.
    :param lst_rezervari: lista de rezervari
    :param nume1: numele cautat
    :return: lista modificata
    """
    result = []
    ok = len(lst_rezervari)
    for rezervare in lst_rezervari:
        clasa = get_clasa(rezervare)
        if get_nume(rezervare) == nume1:
            if clasa == 'economy':
                clasa = 'economy plus'
            elif clasa == 'economy plus':
                clasa = 'business'
        else:
            ok = ok - 1
        result.append(creeaza_rezervare(get_id(rezervare), get_nume(rezervare),
                                        clasa, get_pret(rezervare), get_checkin(rezervare)))
    if ok == 0:
        raise ValueError(f'Nu exista o rezervare cu numele {nume1}.')
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return result

