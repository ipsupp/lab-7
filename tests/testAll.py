from tests.testEveniment import testEveniment, testEveniment_Setteri
from tests.testPersoana import testPersoana, testPersoana_Setteri
from tests.testPersoanaEveniment import testPersoanaEveniment, testPersoanaEveniment_Setteri
from tests.testRepository import test_adauga, test_modifica


def test_all():

    testPersoana()
    testPersoana_Setteri()

    testEveniment()
    testEveniment_Setteri()

    testPersoanaEveniment()
    testPersoanaEveniment_Setteri()

    #test_AdaugaR()
    #test_ModificaR()