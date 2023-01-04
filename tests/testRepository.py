from domain.eveniment import Eveniment
from repositories.Repository import Repository


def test_adauga():
    evenimentRepository = Repository()
    eveniment = Eveniment("01", "20", "70", "bal")

    evenimentRepository.adauga(eveniment)

    evenimente = evenimentRepository.get_all()
    assert len(evenimente) == 1
    assert evenimente[0].get_descriere() == "bal"

    try:
        evenimentRepository.adauga(eveniment)
        assert False
    except KeyError:
        pass

def test_modifica():
    evenimentRepository = Repository()
    eveniment = Eveniment("01", "20", "70", "bal")
    eveniment1 = Eveniment("01", "25", "60", "chef")
    eveniment2 = Eveniment("02", "30", "800", "petrecere")
    evenimentRepository.adauga(eveniment)

    evenimentRepository.modifica(eveniment1)

    evenimente = evenimentRepository.get_all()
    assert evenimente[0].get_data() == "25"

    try:
        evenimentRepository.modifica(eveniment2)
        assert True
    except KeyError:
        ...