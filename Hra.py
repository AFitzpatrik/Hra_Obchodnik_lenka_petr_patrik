
from Osoba import Osoba
from Lokace import Lokace


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
        konec = False
        # nova_lokace = 1
        while not konec:
            try:
                nova_lokace = int(input('Kam chcete přejít? '))
            except ValueError:
                print("zadejte lokaci jako cislo")
                continue
            except:
                continue
            else:
                konec = True
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

    def zacni_obchodovat(self, osoba):
        self.aktualni_lokace.vypis_predmety_akce()
        konec = False
        while not konec:
            try:
                akce = int(input("Vyber akci: "))
            except ValueError as e:
                print(e)
                continue
            if akce == 1:
                konec = False
                while not konec:
                    try:
                        vec = input("Co chces prodat? ")
                    except ValueError:
                        continue
                    else:
                        break
                if self.aktualni_lokace.misto == 'Večerka':
                    osoba.prodej_kabat_batoh(vec, self.aktualni_lokace.predmety)
                else:
                    osoba.prodej_zbozi(vec, self.aktualni_lokace.predmety)
            elif akce == 2:
                konec = False
                while not konec:
                    try:
                        vec = input("Co chces koupit? ")
                    except ValueError:
                        continue
                    else:
                        break
                if self.aktualni_lokace.misto == 'Večerka':
                    osoba.nakup_kabat_batoh(vec, self.aktualni_lokace.predmety)
                else:
                    osoba.nakup_zbozi(vec, self.aktualni_lokace.predmety)
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
        hra.zacni_obchodovat(osoba)
    print(20 * "_")
    print(f"po 14 dnech mas na uctu {osoba.penez} kc")
    jmeno = input("Zadej jmeno: ")
    veta = f"Hrac {jmeno} ma na konci hry na uctu {osoba.penez} Kc"
    try:
        with open("highscores.txt", "w", encoding="utf-8") as f:
            f.write(veta)
        with open("highscores.txt", "r", encoding="utf-8") as f:
            obsah_souboru = f.read()
            print(obsah_souboru)
    except Exception as e:
        print(e)