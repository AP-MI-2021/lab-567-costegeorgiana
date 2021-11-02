from Domain.rezervare import get_pret


def get_ordonare_descrescator_dupa_pret(lst_rezervari):
    """
    Ordoneaza lista de rezervari in ordine descrescatoare dupa pret.
    :param lst_rezervari: lista de rezervari
    :return: lista sortata
    """
    n = len(lst_rezervari)
    for i in range(n-1):
        for j in range(i+1, n):
            if get_pret(lst_rezervari[i]) < get_pret(lst_rezervari[j]):
                aux = lst_rezervari[i]
                lst_rezervari[i] = lst_rezervari[j]
                lst_rezervari[j] = aux
    return lst_rezervari
