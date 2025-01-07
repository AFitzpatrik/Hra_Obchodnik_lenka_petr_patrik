class Hra:
    def __init__(self):
        self.penize = 100
        self.lokace = ['Hradčany', 'Václavák', 'Holešovice' ]
        self.dny = 0
        self.konec_hry = 14

    def presun_do_lokaci(self):
        print('Dostupné lokace:1- Hradčany,2- Václavák,3- Holešovice')

        nova_lokace = int(input('Kam chcete přejít?'))




        self.dny += 1
