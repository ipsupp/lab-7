from repositories.Repository import Repository
from repositories.evenimentFileRepository import FileEvenimentRepository
from repositories.inscrieriFileRepository import FilePersoanaEvenimentRepository
from repositories.persoanaFileRepository import FilePersoanaRepository

from service.evenimentService import EvenimentService
from service.persoanaService import PersoanaService
from service.persoana_evenimenteService import PersoanaEvenimentService
from tests.testAll import test_all
from ui.consola import Consola


def main():
    test_all()
    '''
    persoanaRepository = Repository()
    evenimentRepository = Repository()
    persoanaEvenimentRepository = Repository()

    persoanaService = PersoanaService (persoanaRepository, persoanaEvenimentRepository)
    evenimentService = EvenimentService(evenimentRepository, persoanaEvenimentRepository)
    persoanaEvenimentService = PersoanaEvenimentService(persoanaEvenimentRepository, persoanaRepository, evenimentRepository)
    '''
    persoanaFileRepository = FilePersoanaRepository("persoane.txt")
    evenimentFileRepository = FileEvenimentRepository("evenimente.txt")
    inscrieriFileRepository = FilePersoanaEvenimentRepository("inscrieri.txt")

    persoanaService = PersoanaService (persoanaFileRepository, inscrieriFileRepository)
    evenimentService = EvenimentService (evenimentFileRepository, inscrieriFileRepository)
    persoanaEvenimentService = PersoanaEvenimentService (inscrieriFileRepository, persoanaFileRepository, evenimentFileRepository)

    consola = Consola(persoanaService, evenimentService, persoanaEvenimentService)
    consola.meniu()

    #si termina restul bulinutelor de pe fisa ( ai pe teams exemple la P_E )
main()