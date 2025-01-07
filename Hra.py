class Hra:
    def __init__(self):
        self.penize = 100
        self.lokace = [Lokace('Hradčany'), Lokace('Václavák'), Lokace('Holešovice') ]
        self.aktualni_lokace = self.lokace[0]
        self.dny = 0
        self.konec_hry = 14

    def presun_do_lokaci(self):
        print('Dostupné lokace:1-Hradčany,2- Václavák,3- Holešovice')

        nova_lokace = int(input('Kam chcete přejít?'))
        if nova_lokace == 1:
            self.aktualni_lokace = self.lokace[0]
        elif nova_lokace == 2:
            self.aktualni_lokace = self.lokace[1]
        elif nova_lokace == 3:
            self.aktualni_lokace = self.lokace[2]





        self.dny += 1


class Predmet:
    def __init__(self, nazev, cena):
        self.cena = cena
        self.nazev = nazev


class Lokace:
    def __init__(self, misto):
        self.misto = misto
        self.predmety = [Predmet("Utopenec", 55), Predmet("Med", 100), Predmet("Láhev pálavy", 250)]




class Osoba:
    def __init__(self):
        self.pocet_predmetu = 0
        #self.penez = 100
        self.kabat = False
        self.batoh = False



"""
if __name__ ==  "__main__":
    hradcany = Lokace() 
    hra = Hra()
    hra.presun_do_lokaci()
"""