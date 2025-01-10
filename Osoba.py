from Predmet import Predmet


class Osoba:
    def __init__(self):
        self.pocet_predmetu = 0
        self.muzu_koupit = 2
        self.penez = 500
        self.kabat = False
        self.batoh = False
        self.nakup_kos = {}

    def prodej_kabat_batoh(self, vec: str, predmety: dict[str:Predmet]):
            if vec == "kabat" and not self.kabat:
                print("Nemuzes prodat kabat, kdyz ho nemas")
            elif vec == "batoh" and not self.batoh:
                print("Nemuzes prodat batoh, kdyz ho nemas")
            else:
                if vec == "kabat":
                    self.kabat = False
                    self.muzu_koupit -= 2
                    self.penez += predmety.get(vec).cena
                elif vec == "batoh":
                    self.batoh = False
                    self.muzu_koupit -= 3
                    self.penez += predmety.get(vec).cena

    def nakup_kabat_batoh(self, vec: str, predmety: dict[str:Predmet]):
        if predmety.get(vec).cena > self.penez:
            print(f"Nemas dostatek penez. "
                  f"{vec} stoji {predmety.get(vec).cena} "
                  f"a ty mas {self.penez} Kc")
        else:
            if vec == "kabat":
                self.kabat = True
                self.muzu_koupit += 2
                self.penez -= predmety.get(vec).cena
            elif vec == "batoh":
                self.batoh = True
                self.muzu_koupit += 3
                self.penez -= predmety.get(vec).cena

    def nakup_zbozi(self, vec: str, predmety: dict[str:Predmet]):
        if predmety.get(vec).cena > self.penez:
            print(f"Nemas dostatek penez. "
                  f"{vec} stoji {predmety.get(vec).cena} "
                  f"a ty mas {self.penez} Kc")
        elif self.pocet_predmetu >= self.muzu_koupit:
            print("Nelze koupit další předmět")
        else:
            pocet = self.nakup_kos.get(vec)
            if pocet:
                self.nakup_kos[vec] = pocet + 1
            else:
                self.nakup_kos[vec] = 1
            self.pocet_predmetu += 1
            self.penez -= predmety.get(vec).cena

    def prodej_zbozi(self, vec: str, predmety: dict[str:Predmet]):
        pocet = self.nakup_kos.get(vec)
        if pocet:
            self.nakup_kos[vec] = pocet - 1
            self.penez += predmety.get(vec).cena
            self.pocet_predmetu -= 1
        else:
            print(f"V kosiku neni zadny {vec} na prodani.")

