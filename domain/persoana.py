from domain.entitate import Entitate


class Persoana(Entitate):
    def __init__(self, idPersoana, nume, adresa, inscris, inscrieri):
        super().__init__(idPersoana)
        self.__nume = nume
        self.__adresa = adresa
        self.__inscris = inscris #retine daca persoana participa la vreun eveniment
        self.__inscrieri = inscrieri #retine numarul de evenimente la care participa
    def get_nume(self):
        return self.__nume

    def get_adresa(self):
        return self.__adresa

    def get_inscris(self):
        return self.__inscris

    def get_inscrieri(self):
        return self.__inscrieri

    def set_nume(self, nume):
        self.__nume = nume

    def set_adresa(self, adresa):
        self.__adresa = adresa

    def set_inscris(self, inscris):
        self.__inscris = inscris

    def set_inscrieri(self, inscriere):
        self.__inscrieri = inscriere

    def __str__(self):
        return f' ID_Persoana: {self.get_idEntitate()}, Nume: {self.__nume}, Adresa: {self.__adresa}'
