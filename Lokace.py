
from Predmet import Predmet
import random


class Lokace:
    def __init__(self, misto):
        self.misto = misto
        self.kabat = Predmet("Kabát", 150, 150, 150)
        self.batoh = Predmet("Batoh", 400, 400, 400)
        self.utopenec = Predmet("Utopenec", random.randint(50, 100), 50, 100)
        self.med = Predmet("Med", random.randint(100, 200), 100, 200)
        self.palava = Predmet("Láhev pálavy", random.randint(200, 500), 200, 500)
        if misto == "Večerka":
            self.predmety = {"kabat": self.kabat,
                             "batoh": self.batoh}
        else:
            self.predmety = {"utopenec": self.utopenec,
                             "med": self.med,
                             "palava": self.palava}

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
            if predmet.min_cena <= (predmet.cena + cena_zmenena_o) <= predmet.max_cena:
                predmet.cena = predmet.cena + cena_zmenena_o
