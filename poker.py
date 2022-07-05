import random
class carta:
    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe
        
    def get_numero(self):
        return self.numero
    
    def get_naipe(self):
        return self.naipe
    
    def imprimemao(self):
        print (self.numero, self.naipe)

#Declaração de Variaveis

numerocard = 0
sel = 1
listanaipe = ["Ouro", "Espadas", "Copas", "Paus"]
deck = []
escolha = True
jogadores = []
mesa = []


#Criação de Deck

for naipe in listanaipe:
    for numero in range(1, 14):
        card = carta(numero,naipe)
        deck.append(card)
        

#Embaralhamento de Deck
        
random.shuffle(deck)


#Distribuição de Cartas

numerojogador = int(input("digite o numero de jogadores(2 a 8):"))

while numerojogador < 2 or numerojogador > 8:
    numerojogador = int(input("digite o numero de jogadores(2 a 8):"))
    
for i in range (1, numerojogador+1):
    jogadores.append([])



# distrubuir cartas para jogadores
while sel <= numerojogador:
    
    if numerocard == numerojogador*2:
        break
    if sel == 1:
        jogadores[0].append(deck[numerocard])
    
    elif sel == 2:
        jogadores[1].append(deck[numerocard])
        
    elif sel == 3:
        jogadores[2].append(deck[numerocard])
        
    elif sel == 4:
        jogadores[3].append(deck[numerocard])
        
    elif sel == 5:
        jogadores[4].append(deck[numerocard])
        
    elif sel == 6:
        jogadores[5].append(deck[numerocard])
        
    elif sel == 7:
        jogadores[6].append(deck[numerocard])
       
    elif sel == 8:
        jogadores[7].append(deck[numerocard])
    
    if sel == numerojogador:
        sel = 0

    numerocard += 1    
    sel += 1

#distribuir cartas para a mesa
for j in range(0,5):
    numerocard += 1
    mesa.append(deck[numerocard])



for x,y in enumerate(jogadores):
    print("jogador {}:".format(x+1))
    for z in y:
        z.imprimemao()
        
print("Mesa: ")
for q in mesa:
    q.imprimemao()