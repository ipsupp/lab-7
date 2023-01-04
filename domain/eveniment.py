from domain.entitate import Entitate


class Eveniment(Entitate):
    def __init__(self, idEveniment, data, timp, descriere):
        super().__init__(idEveniment)
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere

    def get_data(self):
        return self.__data

    def get_timp(self):
        return self.__timp

    def get_descriere(self):
        return self.__descriere

    def set_data(self, data):
        self.__data = data

    def set_timp(self, timp):
        self.__timp = timp

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def __str__(self):
        return f' ID_Eveniment: {self.get_idEntitate()}, Data: {self.__data}, Timp: {self.__timp}, Descriere: {self.__descriere}'
