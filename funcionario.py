class funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
        
    def get_nome(self):
        return self.nome
    
    def get_salario(self):
        return self.salario
    
    def exibe_dados(self):
        print ("Nome: {} \nSalario: {}".format(self.nome,self.salario))
        
        
        
class gerente:
    
    def __init__(self,nome,salario):
        funcionario.__init__(self,nome,salario)
    
    def exibe_dados(self):
        print ("Nome: {} \nSalario: {} \nCargo: Gerente".format(self.nome,self.salario))
        
        
        
class assistente:
    
    def __init__(self,nome,salario,matricula):
        funcionario.__init__(self,nome,salario)
        self.matricula = matricula
        
    def exibe_dados(self):
        print ("Nome: {} \nSalario: {} \nCargo: Assistente \nMatricula: {}".format(self.nome,self.salario,self.matricula))
        
        
        
class assistenteTEC:
    
    def __init__(self,nome,salario,matricula,bonus):
        assistente.__init__(self,nome,salario,matricula)
        self.bonus = bonus
        
    def exibe_dados(self):
        print ("Nome: {} \nSalario: {} \nCargo: Assistente \nMatricula: {}".format(self.nome,self.salario,self.matricula))
        print ("Bonus Salarial: {}".format(self.bonus))
        
        
        
class assistenteADMIN:
    
    def __init__(self,nome,salario,matricula,turno):
        assistente.__init__(self,nome,salario,matricula)
        self.turno = turno
        
    
    def exibe_dados(self):
        print ("Nome: {} \nSalario: {} \nCargo: Assistente \nMatricula: {}".format(self.nome,self.salario,self.matricula))
        print ("Turnos: {} e Noturno".format(self.turno))
        
