from Logic.crud import create
from Logic.undo_redo import do_undo, do_redo


def test_undo_redo():
    rezervari = []
    undo_list = []
    redo_list = []
    rezervari = create(rezervari, 1, 'aero567', 'economy', 1234, 'nu', undo_list, redo_list)
    rezervari = create(rezervari, 2, 'aero34', 'business', 2345, 'da', undo_list, redo_list)
    rezervari = create(rezervari, 3, 'aero12', 'economy plus', 3456, 'nu', undo_list, redo_list)
    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 2
    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 1
    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 0
    assert do_undo(undo_list, redo_list, rezervari) is None
    assert len(rezervari) == 0
    rezervari = create(rezervari, 1, 'axe12', 'economy', 1000, 'da', undo_list, redo_list)
    rezervari = create(rezervari, 2, 'axe13', 'economy plus', 1600, 'nu', undo_list, redo_list)
    rezervari = create(rezervari, 3, 'axe14', 'economy plus', 1600.60, 'da', undo_list, redo_list)
    assert do_redo(undo_list, redo_list, rezervari) is None
    assert len(rezervari) == 3
    rezervari = do_undo(undo_list, redo_list, rezervari)
    rezervari = do_undo(undo_list, redo_list, rezervari)
    rezervari = create(rezervari, 4, 'aero14', 'economy', 1601, 'nu', undo_list, redo_list)
    assert do_redo(undo_list, redo_list, rezervari) is None
    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 1
    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 0
    rezervari = do_redo(undo_list, redo_list, rezervari)
    rezervari = do_redo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 2
    assert do_redo(undo_list, redo_list, rezervari) is None
    assert len(rezervari) == 2
