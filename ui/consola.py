from domain.exceptions.duplicateError import DuplicateError
from service.evenimentService import EvenimentService
from service.persoanaService import PersoanaService
from service.persoana_evenimenteService import PersoanaEvenimentService


class Consola:
    def __init__(self, persoanaService: PersoanaService, evenimentService: EvenimentService, persoana_evenimenteService: PersoanaEvenimentService):
        self.__persoanaService = persoanaService
        self.__evenimentService = evenimentService
        self.__persoana_evenimenteService = persoana_evenimenteService

    def adauga_Persoana(self):
        try:
            idPersoana = input("Dati ID-ul persoanei: ")
            nume = input("Dati numele persoanei: ")
            adresa = input("Dati adresa persoanei: ")
            self.__persoanaService.adauga(idPersoana, nume, adresa)
        except KeyError as error:
            print(error)

    def modifica_Persoana(self):
        try:
            idPersoana = input("Dati ID-ul persoanei: ")
            numeNou = input("Dati noul nume al persoanei: ")
            adresa = input("Dati noua adresa persoanei: ")
            self.__persoanaService.modifica(idPersoana, numeNou, adresa)
        except KeyError as error:
            print(error)

    def sterge_Persoana(self):
        try:
            idPersoana = input("Dati ID-ul persoanei: ")
            self.__persoanaService.sterge(idPersoana)
        except KeyError as error:
            print(error)

    def cautare_persoana(self):
        try:
            idPersoana = input("Dati id-ul persoanei: ")
            aux = self.__persoanaService.cauta(idPersoana)
            print(aux)
        except KeyError as error:
            print(error)

    def adauga_Eveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului: ")
            data = input("Dati data evenimentului: ")
            timp = input ("Dati durata in minute ( timp ) a evenimentului: ")
            descriere = input ("Dati o descriere evenimentului: ")
            self.__evenimentService.adauga(idEveniment, data, timp, descriere)
        except KeyError as error:
            print(error)

    def modifica_Eveniment(self):
        try:
            idEveniment= input ("Dati id-ul evenimentului: ")
            dataNoua = input ("Dati noua data a evenimentului: ")
            timpNou = input ("Dati noua durata (timpul) a evenimentului: ")
            descriereNoua = input ("Dati noua descriere a evenimentului: ")
            self.__evenimentService.modifica(idEveniment, dataNoua, timpNou, descriereNoua)
        except KeyError as error:
            print(error)

    def sterge_Eveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului: ")
            self.__evenimentService.sterge(idEveniment)
        except KeyError as error:
            print(error)

    def cautare_eveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului: ")
            aux = self.__evenimentService.cauta(idEveniment)
            print(aux)
        except KeyError as error:
            print(error)

    def adauga_inscriere(self):
        try:
            idPersoanaEveniment = input ("Dati un id inscrierii: ")
            idEveniment = input ("Dati id-ul evenimentului: ")
            idPersoana = input ("Dati id-ul persoanei: ")
            self.__persoana_evenimenteService.adauga_inscriere(idPersoanaEveniment, idPersoana, idEveniment)
        except KeyError as error:
            print(error)
        except DuplicateError as error:
            print(error)

    def sterge_inscriere(self):
        try:
            idPersoana = input ("Dati id-ul persoanei: ")
            idEveniment = input ("Dati id-ul evenimentului: ")
            self.__persoana_evenimenteService.sterge_inscriere(idPersoana, idEveniment)
        except KeyError as error:
            print(error)


    def ordonare_evenimente_dupa_descriere(self):
        rezultat = self.__evenimentService.ordonare_evenimente_dupa_descriere()
        self.afisare(rezultat)

    def ordonare_evenimente_dupa_data(self):
        rezultat = self.__evenimentService.ordonare_evenimente_dupa_data()
        self.afisare(rezultat)

    def participare_persoane(self):
        self.__persoana_evenimenteService.participare_persoane()
        #!!! afisare pt testare only-|
    def afisare(self, entitati):
        for entitate in entitati:
            print(entitate)


    def printMenu(self):
        print("1.  Adauga persoana ")
        print("2.  Modifica persoana ")
        print("3.  Sterge persoana ")
        print("4.  Adauga eveniment")
        print("5.  Modifica eveniment")
        print("6.  Sterge eveniment")
        print("7.  Inscriere persoana la eveniment")
        print("8.  Sterge o inscriere")
        print("9.  Cautare persoana")
        print("10. Cautare eveniment")
        print("11. Ordoneaza evenimentele")
        print("12. Persoane participante la cele mai multe evenimente")
        print("a.  Afiseaza toate persoanele")
        print("b.  Afiseaza toate evenimentele")
        print("c.  Afiseaza toate inscrierile")
        print("x.  Iesire ")

    def printOrdonari(self):
        print("1. Ordoneaza evenimentele dupa descriere")
        print("2. Ordoneaza evenimentele dupa data")


    def meniu(self):
        while True:
            self.printMenu()
            optiune = input("Alegeti optiunea: ")
            if optiune == "1":
                try:
                    self.adauga_Persoana()
                except ValueError as error:
                    print (error)
            elif optiune == "2":
                try:
                    self.modifica_Persoana()
                except ValueError as error:
                    print(error)
            elif optiune == "3":
                try:
                    self.sterge_Persoana()
                except ValueError as error:
                    print(error)
            elif optiune == "4":
                try:
                    self.adauga_Eveniment()
                except ValueError as error:
                    print(error)
            elif optiune == "5":
                try:
                    self.modifica_Eveniment()
                except ValueError as error:
                    print(error)
            elif optiune == "6":
                try:
                    self.sterge_Eveniment()
                except ValueError as error:
                    print(error)
            elif optiune == "7":
                try:
                    self.adauga_inscriere()
                except ValueError as error:
                    print(error)
            elif optiune == "8":
                try:
                    self.sterge_inscriere()
                except ValueError as error:
                    print(error)
            elif optiune == "9":
                self.cautare_persoana()
            elif optiune == "10":
                self.cautare_eveniment()
            elif optiune == "11":
                self.printOrdonari()
                optiune1=input("Alegeti optiunea: ")
                if optiune1 == "1":
                    self.ordonare_evenimente_dupa_descriere()
                elif optiune1 == "2":
                    self.ordonare_evenimente_dupa_data()
            elif optiune == "12":
                self.participare_persoane()
            elif optiune == "13":
                pass
            elif optiune == "a":
                self.afisare(self.__persoanaService.get_all_persoane())
            elif optiune == "b":
                self.afisare(self.__evenimentService.get_all_evenimente())
            elif optiune == "c":
                self.afisare(self.__persoana_evenimenteService.get_all_inscrieri())
            elif optiune == "x":
                print("")
                print("Incheiere program.")
                break
            else:
                print("Optiune invalida, reincercati! ")

