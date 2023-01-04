from domain.persoanaEveniment import PersoanaEveniment


def testPersoanaEveniment():
    inscriere = PersoanaEveniment("001","01","1")

    assert(inscriere.get_idEntitate() == "001")
    assert(inscriere.get_idPersoana() == "01")
    assert(inscriere.get_idEveniment() == "1")

def testPersoanaEveniment_Setteri():
    inscriere = PersoanaEveniment("001","01","1")

    inscriere.set_idEntitate("002")
    assert (inscriere.get_idEntitate() == "002")
    inscriere.set_idPersoana("02")
    assert (inscriere.get_idPersoana() == "02")
    inscriere.set_idEveniment("2")
    assert (inscriere.get_idEveniment() == "2")