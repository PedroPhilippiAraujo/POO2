import random

class jogador:
    def __init__(self, nome, card1, card2):
        self.nome = nome
        self.card1 = card1
        self.card2 = card2
            
    def getnome(self):
        return self.nome
    
    def getcard1(self):
        return self.card1
    
    def getcard2(self):
        return self.card2
#Declaração de Variaveis

numerocard = 0
listanaipe = ["Ouro", "Espadas", "Copas", "Paus"]
deck = []
escolha = True
jogadores = []
mesa = []
fases = ["Preflop", "Flop", "Turn", "River"]
jogadoresativos = []
#Criação de Deck

for naipe in listanaipe:
    for numero in range(1, 14):
        card = f"{numero} {naipe}"
        deck.append(card)
        

#Embaralhamento de Deck
        
random.shuffle(deck)


#numero jogadores

numerojogador = int(input("digite o numero de jogadores(2 a 8):"))

while numerojogador < 2 or numerojogador > 8:
    numerojogador = int(input("digite o numero de jogadores(2 a 8):"))
    




# distrubuir cartas para jogadores

for i in range(0,numerojogador):
    
    if i == 0:
        nome = "Player 1"
        card1 = deck[numerocard]
        card2 = deck[numerocard+1]
        player = jogador(nome, card1, card2)
        
    elif i == 1:
        nome = "Player 2"
        card1 = deck[numerocard]
        card2 = deck[numerocard+1]
        player = jogador(nome, card1, card2)
        
    elif i == 2:
        nome = "Player 3"
        card1 = deck[numerocard]
        card2 = deck[numerocard+1]
        player = jogador(nome, card1, card2)
        
    elif i == 3:
        nome = "Player 4"
        card1 = deck[numerocard]
        card2 = deck[numerocard+1]
        player = jogador(nome, card1, card2)
        
    elif i == 4:
        nome = "Player 5"
        card1 = deck[numerocard]
        card2 = deck[numerocard+1]
        player = jogador(nome, card1, card2)
        
    elif i == 5:
        nome = "Player 6"
        card1 = deck[numerocard]
        card2 = deck[numerocard+1]
        player = jogador(nome, card1, card2)
        
    elif i == 6:
        nome = "Player 7"
        card1 = deck[numerocard]
        card2 = deck[numerocard+1]
        player = jogador(nome, card1, card2)
        
    elif i == 7:
        nome = "Player 8"
        card1 = deck[numerocard]
        card2 = deck[numerocard+1]
        player = jogador(nome, card1, card2)
    
    jogadores.append(player)
    numerocard += 2


#distribuir cartas para a mesa
for j in range(0,5):
    numerocard += 1
    mesa.append(deck[numerocard])


for x in jogadores:
    jogadoresativos.append(x.getnome())

for rodada in fases:
    
    if rodada == "Preflop":
        fim = False
        
        
    if rodada == "Flop":
        print(rodada)
        
    if rodada == "Turn":
        print(rodada)
        
    if rodada == "River":
        print(rodada)

