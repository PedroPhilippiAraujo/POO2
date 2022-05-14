'''
from funcionario import funcionario, gerente, assistente, assistenteTEC, assistenteADMIN

nome = input()
salario = input()

print("Selecione o Cargo:")
print("1 - Funcionario")
print("2 - Gerente")
print("3 - Assistente Técnico")
print("4 - Assistente Administrativo")
x = input()

if x == '1':
    func = funcionario(nome,salario)
    
elif x == '2':
    func = gerente(nome,salario)
    
elif x == '3':
    matricula = input("digite o numero de matricula: ")
    bonus = input("digite o bonus salarial: ")
    func = assistenteTEC(nome, salario, matricula, bonus)
    
elif x == '4':
    matricula = input("digite o numero de matricula: ")
    y = input("escolha o turno de trabalho: \n1 - Matutino \n2 - Vespertino \n")
    
    if y == '1':
        turno = "Matutino"
        
    elif y == '2':
        turno = "Vespertino"
        
    func = assistenteADMIN(nome, salario, matricula, turno)
    

func.exibe_dados()

'''
'''

from ingresso import ingresso, VIP, Normal, CamaroteInferior, CamaroteSuperior 

valor = "1500"
valorextra = "500"
local = "2B"

ticket = CamaroteSuperior(valor,valorextra,local)

ticket.imprimeValor()

'''
from imovel import imovel, novo

valor = 100
valorextra = 50
endereco = "casa da mae joana"

casa = novo(valor,endereco,valorextra)

casa.imprimenovo()