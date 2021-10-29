from Tests.test_clasa_superioara import test_clasa_superioara_pentru_nume
from Tests.test_crud import test_crud
from Tests.test_ieftinire_procentaj import test_ieftinire_procentaj_pentru_checkin
from UserInterface.console import run_ui


def main():
    rezervari = []
    rezervari = run_ui(rezervari)


if __name__ == '__main__':
    test_crud()
    test_clasa_superioara_pentru_nume()
    test_ieftinire_procentaj_pentru_checkin()
    main()
