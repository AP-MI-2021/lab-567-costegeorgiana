from Domain.rezervare import get_checkin, get_pret, creeaza_rezervare, get_id, get_nume, get_clasa


def ieftinire_procentaj_pentru_checkin(lst_rezervari, procentaj: int, undo_list, redo_list):
    """
    Ieftinirea pretului cu un procentaj citit de la tastatura pentru rezervarile la care s-a facut checkin."
    :param redo_list:
    :param lst_rezervari: lista cu rezervari
    :param procentaj: procentajul citit de la tastatura intre 0-100
    :param undo_list:
    :return: lista modificata
    """
    if not (0 <= procentaj <= 100):
        raise ValueError('Procentajul trebuie sa fie intre 0 si 100 inclusiv')
    result = []
    for rezervare in lst_rezervari:
        pret = get_pret(rezervare)
        if get_checkin(rezervare) == 'da':
            pret = pret - (procentaj * pret) // 100

        result.append(creeaza_rezervare(get_id(rezervare), get_nume(rezervare),
                                        get_clasa(rezervare), pret, get_checkin(rezervare)))
    undo_list.append(lst_rezervari)
    redo_list.clear()
    return result
