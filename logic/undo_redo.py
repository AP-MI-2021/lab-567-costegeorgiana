def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    Reface modificarile facute asupra listei.
    :param undo_list: lista dupa undo
    :param redo_list: lista inainte de undo
    :param current_list: lista curenta
    :return: lista modificata
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()
    return None
