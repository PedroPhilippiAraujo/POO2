class ingresso:
    def __init__(self,valor):
        self.valor = int(valor)
        
    def imprimeValor(self):
        print (self.valor)
        
        
class VIP:
    def __init__(self,valor,valorextra):
        ingresso.__init__(self, valor)
        self.valorextra = int(valorextra)
        
    def valorVIP(self):
        print ("Valor do Ingresso VIP: {}".format(self.valor + self.valorextra))
        
        
class Normal(ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        
    def imprimenormal(self):
        print("Ingresso Normal")
        
        

class CamaroteInferior(VIP):
    def __init__(self,valor,valorextra,local):
        super().__init__(valor,valorextra)
        self.local = local
        
    def imprimeLocal(self):
        print (self.local)
        
    
class CamaroteSuperior(VIP):
    def __init__(self,valor,valorextra,local):
        super().__init__(valor,valorextra)
        self.local = local
        
    def imprimeValor(self):
        print("Valor do Camarote: {}".format(self.valor + self.valorextra))
 