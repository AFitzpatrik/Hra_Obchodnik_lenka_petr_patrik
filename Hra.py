
import random


class Osoba:
    def __init__(self):
        self.pocet_predmetu = 0
        self.muzu_koupit = 2
        self.penez = 500
        self.kabat = False
        self.batoh = False
        self.nakup_kos = {}


class Predmet:
    def __init__(self, nazev, cena, min_cena=50, max_cena=500):
        self.cena = cena
        self.min_cena = min_cena
        self.max_cena = max_cena
        self.nazev = nazev

    def __repr__(self):
        return f"{self.nazev} = {self.cena}"
    #def __str__(self):
       # return f"{self.nazev} = {self.cena}"


class Lokace:
    def __init__(self, misto):
        self.misto = misto
        if misto == "Hradčany":
            self.utopenec = Predmet("Utopenec", 60, 50, 100)
            self.med = Predmet("Med", 100, 100, 200)
            self.palava = Predmet("Láhev pálavy", 250, 200, 500)
        elif misto == "Václavák":
            self.utopenec = Predmet("Utopenec", 75, 50, 100)
            self.med = Predmet("Med", 150, 100, 200)
            self.palava = Predmet("Láhev pálavy", 350, 200, 500)
        elif misto == "Holešovice":
            self.utopenec = Predmet("Utopenec", 90, 50, 100)
            self.med = Predmet("Med", 180, 100, 200)
            self.palava = Predmet("Láhev pálavy", 450, 200, 500)
        elif misto == "Večerka":
            self.kabat = Predmet("Kabát", 150, 150, 150)
            self.batoh = Predmet("Batoh", 400, 400, 400)
        if misto == "Večerka":
            self.predmety = {"kabat": self.kabat,
                             "batoh": self.batoh
                             }
        else:
            self.predmety = {"utopenec": self.utopenec,
                             "med": self.med,
                             "palava": self.palava
                            }

    def vypis_predmety_akce(self):
        print("Dostupne predmety:")
        for predmet in self.predmety.values():
            print(predmet)
        print(20 * "_")
        print("Dostupne akce:", "1 Prodej", "2 Nakup",
              "3 prejit jinam", 20 * "_", sep="\n")

    def zmen_ceny(self, predmety: dict[str, Predmet]):
        for predmet in predmety.values():
            cena_zmenena_o = random.randint(-5, 5)
            # print(f"{predmet.nazev}:cena {predmet.cena} + {cena_zmenena_o}.Max cena je {predmet.max_cena} ")
            if predmet.min_cena <= (predmet.cena + cena_zmenena_o) <= predmet.max_cena:
                predmet.cena = predmet.cena + cena_zmenena_o

    def nakup_kabat_batoh(self, vec: str,osoba: Osoba, predmety: dict[str:Predmet]):
        if predmety.get(vec).cena > osoba.penez:
            print(f"Nemas dostatek penez. "
                  f"{vec} stoji {predmety.get(vec).cena} "
                  f"a ty mas {osoba.penez} Kc")
        else:
            if vec == "kabat":
                osoba.kabat = True
                osoba.muzu_koupit += 2
            elif vec == "batoh":
                osoba.batoh = True
                osoba.muzu_koupit += 3

    def nakup(self, vec: str, osoba: Osoba, predmety: dict[str:Predmet]):
        if predmety.get(vec).cena > osoba.penez:
            print(f"Nemas dostatek penez. "
                  f"{vec} stoji {predmety.get(vec).cena} "
                  f"a ty mas {osoba.penez} Kc")
        elif osoba.pocet_predmetu >= osoba.muzu_koupit:
            print("Nelze koupit další předmět")
        else:
            pocet = osoba.nakup_kos.get(vec)
            if pocet:
                osoba.nakup_kos[vec] = pocet + 1
            else:
                osoba.nakup_kos[vec] = 1
            osoba.pocet_predmetu += 1
            osoba.penez -= predmety.get(vec).cena

    def prodej(self, vec: str, osoba: Osoba, predmety: dict[str:Predmet]):
        pocet = osoba.nakup_kos.get(vec)
        if pocet:
            osoba.nakup_kos[vec] = pocet - 1
            osoba.penez += predmety.get(vec).cena
            osoba.pocet_predmetu -= 1
        else:
            print(f"V kosiku neni zadny {vec} na prodani.")


class Hra:
    def __init__(self):
        self.hradcany = Lokace('Hradčany')
        self.vaclavak = Lokace('Václavák')
        self.holesovice = Lokace('Holešovice')
        self.vecerka = Lokace("Večerka")
        self.lokace = [self.hradcany, self.vaclavak, self.holesovice, self.vecerka]
        self.aktualni_lokace = self.lokace[0]
        self.dny = 1

    def presun_do_lokace(self):
        print("""Dostupné lokace:
1- Hradčany
2- Václavák
3- Holešovice
4- Večerka""")
        print(20 * "_")
        nova_lokace = int(input('Kam chcete přejít? '))
        if nova_lokace == 1:
            self.aktualni_lokace = self.lokace[0]
        elif nova_lokace == 2:
            self.aktualni_lokace = self.lokace[1]
        elif nova_lokace == 3:
            self.aktualni_lokace = self.lokace[2]
        elif nova_lokace == 4:
            self.aktualni_lokace = self.lokace[3]
        self.aktualni_lokace.zmen_ceny(self.aktualni_lokace.predmety)
        self.dny += 1

    def nakup_prodej(self, osoba):
        self.aktualni_lokace.vypis_predmety_akce()
        konec = False
        while not konec:
            akce = int(input("Vyber akci: "))
            if akce == 1:
                vec = input("Co chces prodat? ")
                self.aktualni_lokace.prodej(vec, osoba,
                                            self.aktualni_lokace.predmety)
            elif akce == 2:
                vec = input("Co chces koupit? ")
                if self.aktualni_lokace.misto == 'Večerka':
                    self.aktualni_lokace.nakup_kabat_batoh(vec, osoba,
                                               self.aktualni_lokace.predmety)
                else:
                    self.aktualni_lokace.nakup(vec, osoba,
                                           self.aktualni_lokace.predmety)
            elif akce == 3:
                konec = True


if __name__ == "__main__":
    hra = Hra()
    osoba = Osoba()
    while hra.dny <= 14:
        print(20 * "_", 20 * "_", sep='\n')
        print(f"den: {hra.dny}")
        print(f"mas k dispozici {osoba.penez} Kc")
        print(f"v nakupnim kosiku mas {osoba.nakup_kos}")
        hra.presun_do_lokace()
        hra.nakup_prodej(osoba)
    print(20 * "_")
    print(f"po 14 dnech mas na uctu {osoba.penez} kc")





###############################################################################
"""
import random

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
        self.cena = cena + random.randint(-5, 5)
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




if __name__ ==  "__main__":
    hradcany = Lokace() 
    hra = Hra()
    hra.presun_do_lokaci()
"""