from domain.exceptions.duplicateError import DuplicateError
from domain.persoanaEveniment import PersoanaEveniment
from repositories.Repository import Repository

class PersoanaEvenimentService:
    def __init__(self, persoanaEvenimentRepository: Repository, persoanaRepository: Repository, evenimentRepository: Repository):
        self.__persoanaEvenimentRepository = persoanaEvenimentRepository
        self.__persoanaRepository = persoanaRepository
        self.__evenimentRepository = evenimentRepository

    def adauga_inscriere(self, idPersoanaEveniment, idPersoana, idEveniment):
        '''
        adauga in dictionar o inscriere
        :param idPersoanaEveniment: string
        :param idPersoana: string
        :param idEveniment: string
        :return:
        '''
        if self.__persoanaRepository.get_by_ID(idPersoana) is None:
            raise KeyError("Nu exista o persoana cu id-ul dat!")

        if self.__evenimentRepository.get_by_ID(idEveniment) is None:
            raise KeyError("Nu exista un eveniment cu id-ul dat!")

        inscrieri = self.__persoanaEvenimentRepository.get_all()

        for inscriere in inscrieri:
            if inscriere.get_idPersoana() == idPersoana and inscriere.get_idEveniment() == idEveniment:
                raise DuplicateError("Persoana este deja inscrisa la acest eveniment!")

        inscriere = PersoanaEveniment(idPersoanaEveniment, idPersoana, idEveniment)
        self.__persoanaEvenimentRepository.adauga(inscriere)

    def get_all_inscrieri(self):
        '''
        returneaza o lista de inscrieri
        :return: lista de inscrieri
        '''
        return self.__persoanaEvenimentRepository.get_all()

    def sterge_inscriere(self, idPersoana, idEveniment):
        '''
        sterge o inscriere dupa id
        :param idPersoana: string
        :param idEveniment: string
        :return:
        '''
        inscrieri = self.__persoanaEvenimentRepository.get_all()
        for inscriere in inscrieri:
            if inscriere.get_idPersoana() == idPersoana and inscriere.get_idEveniment() == idEveniment:
                self.__persoanaEvenimentRepository.sterge(inscriere.get_idEntitate())

    def participare_persoane(self):
        inscrieri = self.__persoanaEvenimentRepository.get_all()
        inscrieri.sort(key=lambda z: z.get_idPersoana())

        # return inscrieri - BUN

        lst1 = [0 for zero in range(len(inscrieri))]
        lst2 = [0 for zero in range(len(inscrieri))]
        #print(lst2) - BUN
        i = 0
        a=inscrieri[0].get_idPersoana()

        print("Var a =",a) # BUN
        for inscriere in inscrieri:
            lst1[inscriere.get_idPersoana()]



            '''if lst1[i] != inscriere.get_idPersoana():
                lst1[i] = inscrieri[i].get_idPersoana()
                a = lst1[i]
            if lst1[i] != inscriere.get_idPersoana():
                i += 1
            if inscriere.get_idPersoana() == a:
                lst2[i] += 1
            '''
        print(lst1,lst2)