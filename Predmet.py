

class Predmet:
    def __init__(self, nazev, cena, min_cena=50, max_cena=500):
        self.cena = cena
        self.min_cena = min_cena
        self.max_cena = max_cena
        self.nazev = nazev

    #def __repr__(self):
       # return f"{self.nazev} = {self.cena}"
    def __str__(self):
        return f"{self.nazev} = {self.cena}"