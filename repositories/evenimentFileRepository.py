from domain.eveniment import Eveniment
from repositories.Repository import Repository

class FileEvenimentRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, eveniment):
        super().adauga(eveniment)
        self.__writeFile()

    def modifica(self, eveniment):
        super().modifica(eveniment)
        self.__writeFile()

    def sterge(self, eveniment):
        super().sterge(eveniment)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:

                idEveniment = line.split()[0]
                data = line.split()[1]
                timp = line.split()[2]
                descriere = line.split()[3]

                eveniment = Eveniment(idEveniment, data, timp, descriere)
                self._entitati[idEveniment] = eveniment

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for eveniment in self.get_all():
                f.write(f'{eveniment.get_idEntitate()} {eveniment.get_data()} {eveniment.get_timp()} {eveniment.get_descriere()} \n')


