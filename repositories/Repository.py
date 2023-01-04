class Repository:
    def __init__(self):
        self._entitati = {}

    def get_all(self):
        '''
        returneaza o lista de entitati
        :return:  o lista de obiecte de tipul entitate
        '''
        return list(self._entitati.values())

    def get_by_ID(self, idEntitate):
        '''
        returneaza entitatea cu id-ul cerut
        :param idEntitate: string
        :return: un obiect de tipul entitate, daca exista unul, altfel None
        '''
        if idEntitate in self._entitati:
            return self._entitati[idEntitate]
        return None

    def adauga(self, entitate):
        '''
        adauga o entitate in dictionar
        :param entitate: obiect de tipul entitate
        :return:
        '''
        if self.get_by_ID(entitate.get_idEntitate()) is not None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self._entitati[entitate.get_idEntitate()] = entitate

    def modifica(self, entitateNoua):
        '''
        modifica o entitate dupa id
        :param entitateNoua: obiect de tipul entitate
        :return:
        '''
        if self.get_by_ID(entitateNoua.get_idEntitate()) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self._entitati[entitateNoua.get_idEntitate()] = entitateNoua

    def sterge(self, idEntitate):
        '''
        sterge o entiate dupa id
        :param idEntitate: string
        :return:
        '''
        if self.get_by_ID(idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self._entitati.pop(idEntitate)

    def cautare(self, idEntitate):
        '''
        cauta o entitate dupa id
        :param idEntitate: string
        :return: un obiect de tipul entitate daca exista, altfel None
        '''
        entitati = self.get_all()
        for entitate in entitati:
            if entitate.get_idEntitate() == idEntitate:
                return entitate

        return None
