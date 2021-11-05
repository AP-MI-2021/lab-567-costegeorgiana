from Tests.test_clasa_superioara import test_clasa_superioara_pentru_nume
from Tests.test_crud import test_crud
from Tests.test_ieftinire_procentaj import test_ieftinire_procentaj_pentru_checkin
from UserInterface.command_line_console import run_ui_line_console
# from UserInterface.console import run_ui
from Tests.test_crud import get_data


def main():
    rezervari = get_data()
    rezervari = run_ui_line_console(rezervari)


if __name__ == '__main__':
    test_crud()
    test_clasa_superioara_pentru_nume()
    test_ieftinire_procentaj_pentru_checkin()
    main()
