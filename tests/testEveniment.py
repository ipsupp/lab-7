from domain.eveniment import Eveniment


def testEveniment():
    eveniment = Eveniment("01","20","70","bal")

    assert eveniment.get_idEntitate() == "01"
    assert eveniment.get_data() == "20"
    assert eveniment.get_timp() == "70"
    assert eveniment.get_descriere() == "bal"

def testEveniment_Setteri():
    eveniment = Eveniment("01", "20", "70", "bal")

    eveniment.set_idEntitate("02")
    assert eveniment.get_idEntitate() == "02"

    eveniment.set_data("21")
    assert eveniment.get_data() == "21"

    eveniment.set_timp("30")
    assert eveniment.get_timp() == "30"

    eveniment.set_descriere("petrecere")
    assert eveniment.get_descriere() == "petrecere"