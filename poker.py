import random

class jogador:
    def __init__(self, nome, card1, card2):
        self.nome = nome
        self.card1 = card1
        self.card2 = card2
        self.carteira = 300
        self.aposta = 0
   
    def getnome(self):
        return self.nome
    
    def getcarteira(self):
        return self.carteira
    
    def getaposta(self):
        return self.aposta
    
    def bet(self, bet):
        self.carteira = self.carteira - bet
        self.aposta = self.aposta + bet
        
    def imprimemao(self):
        print(self.card1)
        print(self.card2)
        
    def venceu(self, pote):
        self.carteira = self.carteira + pote
    
#Declaração de Variaveis

numerocard = 0
listanaipe = ["Ouro", "Espadas", "Copas", "Paus"]
deck = []
escolha = True
jogadores = []
mesa = []
fases = ["Preflop", "Flop", "Turn", "River"]
jogadoresativos = []
pote = 0
visualizar = True
#Criação de Deck

for naipe in listanaipe:
    for numero in range(1, 14):
        card = f"{numero} {naipe}"
        deck.append(card)
        

#Embaralhamento de Deck
        
random.shuffle(deck)


#numero jogadores

numerojogador = int(input("digite o numero de jogadores(2 a 8): "))

while numerojogador < 2 or numerojogador > 8:
    numerojogador = int(input("digite o numero de jogadores(2 a 8): "))
    




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

#lista de jogadores ativos
for x in jogadores:
    jogadoresativos.append(x.getnome())

#Ver cartas de cada Jogador
while visualizar == True:
    search = input("Digite o nome do jogador que deseja ver a mão ou 0 para sair: ")  
    if search == '0':
        visualizar = False
        
    else:
        for k in jogadores:
            if k.getnome() == search:
                k.imprimemao()
        
        
        
        
        
#Rodada de Apostas
for rodada in fases:
    
    if rodada == "Preflop":
        print (rodada)
        fim = False
        check = 10
        while fim == False:
            for k in jogadores:
                for l in jogadoresativos:
                    if k.getnome() == l:
                        print(l,":")
                        print("Check: ",check)
                        print("Aposta: ",k.getaposta())
                        print("O que você deseja fazer?")
                    
                        if k.getaposta() < check:
                            print("1-Call")
                            print("2-Raise")
                            print("3 - Fold")
                            sel = int(input())
                        
                            if sel == 1:
                                k.bet(check-k.getaposta())
                            
                            elif sel == 2:
                                print("Digite o quanto deseja aumentar: ")
                                print("1-{} / 2-{} / 3-{} / 4-{} / 5- {} / 6 - All In".format(check*2, check*4, check*6, check*8, check*10))
                                choice = int(input())
                                if choice >= 1 and choice <= 5:
                                    k.bet(check*choice*2)
                                elif choice == 6:
                                    k.bet(k.getcarteira())
                                check = k.getaposta()
                            
                            elif sel == 3:
                                jogadoresativos.remove(l)
                                    
                        elif k.getaposta() == check:
                            print("1-check")
                            print("2-Raise")
                            sel = int(input())
                            
                            if sel == 2:
                                print("Digite o quanto deseja aumentar: ")
                                print("1-{} / 2-{} / 3-{} / 4-{} / 5- {} / 6 - All In".format(check*2, check*4, check*6, check*8, check*10))
                                choice = int(input())
                                if choice >= 1 and choice <= 5:
                                    k.bet(check*choice*2)
                                elif choice == 6:
                                    k.bet(k.getcarteira())
                                check = k.getaposta()
        
        
        
            fim = True
            for k in jogadores:
                for l in jogadoresativos:
                    if k.getnome() == l:
                        if k.getaposta() < check:
                            fim = False
        
        for k in jogadores:
            pote += k.getaposta()
        
        
    elif rodada == "Flop":
        print(rodada)
        print("Pote: ",pote)
        print("Cartas na Mesa")
        print(mesa[0:3])
        fim = False
        check = 0
        while fim == False:
            for k in jogadores:
                for l in jogadoresativos:
                    if k.getnome() == l:
                        print(l,":")
                        print("Check: ",check)
                        print("Aposta: ",k.getaposta())
                        print("O que você deseja fazer?")
                    
                        if k.getaposta() < check:
                            print("1-Call")
                            print("2-Raise")
                            print("3 - Fold")
                            sel = int(input())
                        
                            if sel == 1:
                                k.bet(check-k.getaposta())
                            
                            elif sel == 2:
                                print("Digite o quanto deseja aumentar: ")
                                print("1-{} / 2-{} / 3-{} / 4-{} / 5- {} / 6 - All In".format(check*2, check*4, check*6, check*8, check*10))
                                choice = int(input())
                                if choice >= 1 and choice <= 5:
                                    k.bet(check*choice*2)
                                elif choice == 6:
                                    k.bet(k.getcarteira())
                                check = k.getaposta()
                            
                            elif sel == 3:
                                jogadoresativos.remove(l)
                                    
                        elif k.getaposta() == check or check == 0:
                            print("1-check")
                            print("2-Raise")
                            sel = int(input())
                            
                            if sel == 2:
                                print("Digite o quanto deseja aumentar: ")
                                print("1-{} / 2-{} / 3-{} / 4-{} / 5- {} / 6 - All In".format(check*2, check*4, check*6, check*8, check*10))
                                choice = int(input())
                                if choice >= 1 and choice <= 5:
                                    k.bet(check*choice*2)
                                elif choice == 6:
                                    k.bet(k.getcarteira())
                                check = k.getaposta()
        
        
        
            fim = True
            for k in jogadores:
                for l in jogadoresativos:
                    if k.getnome() == l:
                        if k.getaposta() < check:
                            fim = False
        
        pote = 0
        for k in jogadores:
            pote += k.getaposta()
            
            
    elif rodada == "Turn":
        print(rodada)
        print("Pote: ",pote)
        print("Cartas na Mesa")
        print(mesa[0:4])
        fim = False
        check = 0
        while fim == False:
            for k in jogadores:
                for l in jogadoresativos:
                    if k.getnome() == l:
                        print(l,":")
                        print("Check: ",check)
                        print("Aposta: ",k.getaposta())
                        print("O que você deseja fazer?")
                    
                        if k.getaposta() < check:
                            print("1-Call")
                            print("2-Raise")
                            print("3 - Fold")
                            sel = int(input())
                        
                            if sel == 1:
                                k.bet(check-k.getaposta())
                            
                            elif sel == 2:
                                print("Digite o quanto deseja aumentar: ")
                                print("1-{} / 2-{} / 3-{} / 4-{} / 5- {} / 6 - All In".format(check*2, check*4, check*6, check*8, check*10))
                                choice = int(input())
                                if choice >= 1 and choice <= 5:
                                    k.bet(check*choice*2)
                                elif choice == 6:
                                    k.bet(k.getcarteira())
                                check = k.getaposta()
                            
                            elif sel == 3:
                                jogadoresativos.remove(l)
                                    
                        elif k.getaposta() == check or check == 0:
                            print("1-check")
                            print("2-Raise")
                            sel = int(input())
                            
                            if sel == 2:
                                print("Digite o quanto deseja aumentar: ")
                                print("1-{} / 2-{} / 3-{} / 4-{} / 5- {} / 6 - All In".format(check*2, check*4, check*6, check*8, check*10))
                                choice = int(input())
                                if choice >= 1 and choice <= 5:
                                    k.bet(check*choice*2)
                                elif choice == 6:
                                    k.bet(k.getcarteira())
                                check = k.getaposta()
        
        
        
            fim = True
            for k in jogadores:
                for l in jogadoresativos:
                    if k.getnome() == l:
                        if k.getaposta() < check:
                            fim = False
        
        pote = 0
        for k in jogadores:
            pote += k.getaposta()
            
            
    elif rodada == "River":
        print(rodada)
        print("Pote: ",pote)
        print("Cartas na Mesa")
        print(mesa[0:5])
        fim = False
        check = 0
        while fim == False:
            for k in jogadores:
                for l in jogadoresativos:
                    if k.getnome() == l:
                        print(l,":")
                        print("Check: ",check)
                        print("Aposta: ",k.getaposta())
                        print("O que você deseja fazer?")
                    
                        if k.getaposta() < check:
                            print("1-Call")
                            print("2-Raise")
                            print("3 - Fold")
                            sel = int(input())
                        
                            if sel == 1:
                                k.bet(check-k.getaposta())
                            
                            elif sel == 2:
                                print("Digite o quanto deseja aumentar: ")
                                print("1-{} / 2-{} / 3-{} / 4-{} / 5- {} / 6 - All In".format(check*2, check*4, check*6, check*8, check*10))
                                choice = int(input())
                                if choice >= 1 and choice <= 5:
                                    k.bet(check*choice*2)
                                elif choice == 6:
                                    k.bet(k.getcarteira())
                                check = k.getaposta()
                            
                            elif sel == 3:
                                jogadoresativos.remove(l)
                                    
                        elif k.getaposta() == check or check == 0:
                            print("1-check")
                            print("2-Raise")
                            sel = int(input())
                            
                            if sel == 2:
                                print("Digite o quanto deseja aumentar: ")
                                print("1-{} / 2-{} / 3-{} / 4-{} / 5- {} / 6 - All In".format(check*2, check*4, check*6, check*8, check*10))
                                choice = int(input())
                                if choice >= 1 and choice <= 5:
                                    k.bet(check*choice*2)
                                elif choice == 6:
                                    k.bet(k.getcarteira())
                                check = k.getaposta()
        
        
        
            fim = True
            for k in jogadores:
                for l in jogadoresativos:
                    if k.getnome() == l:
                        if k.getaposta() < check:
                            fim = False
        
        pote = 0
        for k in jogadores:
            pote += k.getaposta()


#Print Final de todos os Resultados
print(mesa)
for g in jogadores:
    for h in jogadoresativos:
        if g.getnome() == h:
            print(g.getnome())
            g.imprimemao()

#Escolha do Vencedor            
vencedor = input("Digite o nome do Vencedor: ")
for g in jogadores:
    if g.getnome() == vencedor:
        g.venceu(pote)
