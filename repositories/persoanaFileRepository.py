from domain.persoana import Persoana
from repositories.Repository import Repository

class FilePersoanaRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, persoana):
        super().adauga(persoana)
        self.__writeFile()

    def modifica(self, persoana):
        super().modifica(persoana)
        self.__writeFile()

    def sterge(self, persoana):
        super().sterge(persoana)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:

                idPersoana = line.split()[0]
                nume = line.split()[1]
                adresa = line.split()[2]
                inscris = line.split()[3]
                inscriere = line.split()[4]

                persoana = Persoana(idPersoana, nume, adresa, inscris, inscriere)
                self._entitati[idPersoana] = persoana

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for persoana in self.get_all():
                f.write(f'{persoana.get_idEntitate()} {persoana.get_nume()} {persoana.get_adresa()} \n')


