class imovel:
    def __init__(self,valor,endereco):
        self.valor = int(valor)
        self.endereco = endereco
        
        
        
class novo(imovel):
    def __init__(self,valor,endereco,valorextra):
        super().__init__(valor,endereco)
        self.valorextra = int(valorextra)
        
    def imprimenovo(self):
        print("Endereço: {} \nValor: {}".format(self.endereco, self.valor + self.valorextra))