from domain.persoana import Persoana
from repositories.Repository import Repository


class PersoanaService:

    def __init__(self, persoanaRepository: Repository, persoanaEvenimentRepository: Repository):
        self.__persoanaRepository = persoanaRepository
        self.__persoanaEvenimentRepository = persoanaEvenimentRepository

    def get_all_persoane(self):
        '''
        returneaza o lista de persoane
        :return:
        '''
        return self.__persoanaRepository.get_all()
#comm
    def adauga(self, idPersoana, nume, adresa):
        '''
        adauga in dictionar o persoana
        :param idPersoana: string
        :param nume: string
        :param adresa: string
        :return:
        '''
        persoana = Persoana(idPersoana, nume, adresa)
        self.__persoanaRepository.adauga(persoana)

    def modifica(self, idPersoana, numeNou, adresaNoua):
        '''
        modifica o persoana dupa id
        :param idPersoana: string
        :param numeNou: string
        :param adresaNoua: string
        :return:
        '''
        persoanaNoua = Persoana(idPersoana, numeNou, adresaNoua)
        self.__persoanaRepository.modifica(persoanaNoua)

    def sterge(self, idPersoana):
        '''
        sterge o persoana dupa id
        :param idPersoana: string
        :return:
        '''
        inscrieri = self.__persoanaEvenimentRepository.get_all()
        for inscriere in inscrieri:
            if inscriere.get_idPersoana() == idPersoana:
                self.__persoanaEvenimentRepository.sterge(inscriere.get_idEntitate())
        self.__persoanaRepository.sterge(idPersoana)

    def cauta(self, idPersoana):
        '''
        cauta o persoana dupa id
        :param idPersoana: string
        :return: persoana cautata daca exista, altfel None
        '''
        aux = self.__persoanaRepository.cautare(idPersoana)
        if aux == None:
            raise Exception("Nu exista aceasta persoana!")
        else:
            return aux
