from domain.entitate import Entitate


class PersoanaEveniment(Entitate):

    def __init__(self, idPersoanaEveniment, idPersoana, idEveniment):
        super().__init__(idPersoanaEveniment)
        self.__idPersoana = idPersoana
        self.__idEveniment = idEveniment

    def get_idPersoana(self):
        return self.__idPersoana

    def get_idEveniment(self):
        return self.__idEveniment

    def set_idPersoana(self, idPersoana):
        self.__idPersoana = idPersoana

    def set_idEveniment(self, idEveniment):
        self.__idEveniment = idEveniment

    def __str__(self):
        return f' ID_Inscriere: {self.get_idEntitate()}, ID_Persoana: {self.__idPersoana}, ID_Eveniment: {self.__idEveniment}'