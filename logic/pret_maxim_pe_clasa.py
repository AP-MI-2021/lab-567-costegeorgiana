from Domain.rezervare import get_clasa, get_pret


def pret_maxim_per_clasa(lst_rezervari):
    """
    Determina pretul maxim pentru fiecare clasa.
    :param lst_rezervari: lista de rezervari.
    :return: un dictionar in care cheia este clasa, iar valoarea
            este rezervarea cu pretul maxim care are acea clasa.
    """
    result = {}
    for rezervare in lst_rezervari:
        clasa = get_clasa(rezervare)
        pret = get_pret(rezervare)
        if clasa not in result:
            result[clasa] = pret
        elif pret > result[clasa]:
            result[clasa] = pret
    return result
