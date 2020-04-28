import random

class Baraja():
    palos = ["o","c","e","b"]
    cartas = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]

    def __init__(self):
        self.baraja =[]
        self.mano = []
        for palo in self.palos:
            for carta in self.cartas:
                naipe = carta + palo
                self.naipes.append(naipe)


    def mezclar(self):
        br = []
        while len(self.naipes) != len(br):
            n = random.randint(0,len(self.naipes)-1)
            while self.naipes[n] in br:
                n = random.randint(0,len(self.naipes)-1)
            br.append(self.naipes[n])   
        self.naipes[:] = br


    def repartir(self,players,cards):
        self.mano = []
        for p in range(players):
            self.mano.append([])

        for ic in range(cards):
            for ij in range(players):
                carta = self.naipes.pop(0)
                self.mano[ij].append(carta)

