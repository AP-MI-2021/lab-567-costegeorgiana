from Domain.rezervare import get_nume, get_pret


def sume_preturi_pentru_nume(lst_rezervari):
    """
    Determina suma preturilor pentru fiecare nume.
    :param lst_rezervari: lista de rezervari
    :return:un dictionar in care cheia este numele,/
            iar valoarea este suma preturilor rezervarilor cu acelasi nume."
    """
    result = {}
    for rezervare in lst_rezervari:
        nume = get_nume(rezervare)
        pret = get_pret(rezervare)
        if nume not in result:
            result[nume] = pret
        else:
            result[nume] += pret
    return result
