from Tests.test_clasa_superioara import test_clasa_superioara_pentru_nume
from Tests.test_crud import test_crud
from Tests.test_ieftinire_procentaj import test_ieftinire_procentaj_pentru_checkin
from Tests.test_undo_redo import test_undo_redo
from UserInterface.command_line_console import run_ui_line_console
from UserInterface.console import run_ui
from Logic.crud import create


def main():
    rezervari = []
    redo_list = []
    undo_list = []
    rezervari = create(rezervari, 1, 'axe12', 'economy', 1000, 'da', undo_list, redo_list)
    rezervari = create(rezervari, 2, 'axe13', 'economy plus', 1600, 'nu', undo_list, redo_list)
    rezervari = create(rezervari, 3, 'axe14', 'economy plus', 1600.60, 'da', undo_list, redo_list)
    rezervari = create(rezervari, 4, 'axe12', 'business', 3000, 'nu', undo_list, redo_list)
    rezervari = create(rezervari, 5, 'axe13', 'economy', 1000.80, 'da', undo_list, redo_list)
    print(f'Alegeti interfata pe care vreti sa lucrati:')
    print(f'1.CONSOLE')
    print(f'2.COMMAND LINE CONSOLE')
    optiune = input('Introdu optiunea: ')
    if optiune == '1':
        rezervari = run_ui(rezervari, undo_list, redo_list)
    elif optiune == '2':
        rezervari = run_ui_line_console(rezervari)


if __name__ == '__main__':
    test_crud()
    test_clasa_superioara_pentru_nume()
    test_ieftinire_procentaj_pentru_checkin()
    test_undo_redo()
    main()
