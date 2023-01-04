from domain.persoanaEveniment import PersoanaEveniment
from repositories.Repository import Repository

class FilePersoanaEvenimentRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, inscriere):
        super().adauga(inscriere)
        self.__writeFile()

    def modifica(self, inscriere):
        super().modifica(inscriere)
        self.__writeFile()

    def sterge(self, inscriere):
        super().sterge(inscriere)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idPersoanaEveniment = line.split()[0]
                idPersoana = line.split()[1]
                idEveniment = line.split()[2]
                inscriere = PersoanaEveniment(idPersoanaEveniment, idPersoana, idEveniment)
                self._entitati[idPersoanaEveniment] = inscriere

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for inscriere in self.get_all():
                f.write(f'{inscriere.get_idEntitate()} {inscriere.get_idPersoana()} {inscriere.get_idEveniment()} \n')


