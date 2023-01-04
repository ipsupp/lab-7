from domain.persoana import Persoana


def testPersoana():
    persoana = Persoana("00", "Maria", "Lalea")

    assert persoana.get_idEntitate() == "00"
    assert persoana.get_nume() == "Maria"
    assert persoana.get_adresa() == "Lalea"


def testPersoana_Setteri():
    persoana = Persoana("00", "Maria", "Lalea")

    persoana.set_idEntitate("01")
    assert persoana.get_idEntitate() == "01"

    persoana.set_nume("Ana")
    assert persoana.get_nume() == "Ana"

    persoana.set_adresa("Jupiter")
    assert persoana.get_adresa() == "Jupiter"
