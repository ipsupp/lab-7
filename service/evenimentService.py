from domain.eveniment import Eveniment
from repositories.Repository import Repository


class EvenimentService:
    def __init__(self, evenimentRepository: Repository, persoanaEvenimentRepository: Repository):
        self.__evenimentRepository = evenimentRepository
        self.__persoanaEvenimentRepository = persoanaEvenimentRepository

    def get_all_evenimente(self):
        '''
        returneaza o lista de evenimente
        :return:
        '''
        return self.__evenimentRepository.get_all()

    def adauga(self, idEveniment, data, timp, descriere):
        '''
        adauga un eveniment in lista
        :param idEveniment: string
        :param data: string
        :param timp: int
        :param descriere: string
        :return:
        '''
        eveniment = Eveniment(idEveniment, data, timp, descriere)
        self.__evenimentRepository.adauga(eveniment)

    def modifica(self, idEveniment, dataNoua, timpNou, descriereNoua):
        '''
        modifica un eveniment dupa id
        :param idEveniment: string
        :param dataNoua: string
        :param timpNou: int
        :param descriereNoua: string
        :return:
        '''
        evenimentNou = Eveniment(idEveniment, dataNoua, timpNou, descriereNoua)
        self.__evenimentRepository.modifica(evenimentNou)

    def sterge(self, idEveniment):
        '''
        sterge un eveniment dupa id
        :param IDE: string
        :return:
        '''
        inscrieri = self.__persoanaEvenimentRepository.get_all()
        for inscriere in inscrieri:
            if inscriere.get_idEveniment() == idEveniment:
                self.__persoanaEvenimentRepository.sterge(inscriere.get_idEntitate())
        self.__evenimentRepository.sterge(idEveniment)


    def cauta(self, idEveniment):
        '''
        cauta un obiect dupa id
        :param idEveniment: string
        :return: evenimentul cautat daca exista, altfel None
        '''
        aux = self.__evenimentRepository.cautare(idEveniment)
        if aux == None:
            raise Exception("Nu exista aceast eveniment!")
        else:
            return aux
    def ordonare_evenimente_dupa_descriere(self):
        lst = []
        evenimente = self.__evenimentRepository.get_all()
        for eveniment in evenimente:
            lst.append(eveniment)
        lst.sort(key = lambda x: x.get_descriere())
        return lst

    def ordonare_evenimente_dupa_data(self):
        lst = []
        evenimente = self.__evenimentRepository.get_all()
        for eveniment in evenimente:
            lst.append(eveniment)
        lst.sort(key = lambda y: y.get_data())
        return lst
