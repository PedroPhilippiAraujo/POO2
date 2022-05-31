'''
#1
x = True

while x == True:
    num = float(input("digite um numero: "))
    if num >= 0 and num <= 10:
        x = False
'''
'''
#2
x = True

while x == True:
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    if nome != senha:
        x = False
'''

'''
#3
a = True
b = True
c = True
d = True
e = True

while a == True:
    nome = input("Digite o nome: ")
    if len(nome) > 3:
        a = False
        
while b == True:
    idade = int(input("Digite a idade: "))
    if idade > 0 and idade < 150:
        b = False
        
while c == True:
    salario = int(input("Digite o salario: "))
    if salario > 0:
        c = False
               
while d == True:
    sexo = input("Digite o sexo(m/f): ")
    if sexo == 'f' or sexo == 'm':
        d = False
 
while e == True:
    estado = input("Digite o estado civil(s/c/v/d): ")
    if estado == 's' or estado == 'c' or estado == 'v' or estado == 'd':
        e = False
'''


'''
#4
cidadeA = 80000
cidadeB = 200000
anos = 0
x = True 

while x == True:
    anos += 1
    cidadeA = cidadeA * 1.03
    cidadeB = cidadeB * 1.015
    if cidadeA >= cidadeB:
        x = False
        
print(anos)

'''


'''
#5
cidadeA = float(input("Digite a população da cidade A: "))
while cidadeA <= 0:
    cidadeA = float(input("Digite a população da cidade A: "))
    
taxaA = (float(input("Digite a taxa de crescimento da cidade A (em porcentagem): "))+100)/100 
while taxaA < 1:
    taxaA = float(input("Digite a taxa de crescimento da cidade A (em porcentagem): "))/100 


cidadeB = float(input("Digite a população da cidade B: "))
while cidadeB <= 0 or cidadeB < cidadeA:
    cidadeB = float(input("Digite a população da cidade B: "))


taxaB = (float(input("Digite a taxa de crescimento da cidade B (em porcentagem): "))+100)/100 
while taxaB > taxaA or taxaB < 1:
    taxaB = float(input("Digite a taxa de crescimento da cidade B (em porcentagem): "))/100 


anos = 0
x = True 

while x == True:
    anos += 1
    cidadeA = cidadeA * taxaA
    cidadeB = cidadeB * taxaB
    if cidadeA >= cidadeB:
        x = False
        
print(anos)
'''

'''
#6
for i in range (1,21):
    print(i, end=' ')
'''
'''
#7
print("Digite 5 Numeros:")
a = float(input("1: "))
b = float(input("2: "))
c = float(input("3: "))
d = float(input("4: "))
e = float(input("5: "))


num = [a, b, c, d, e]

maior = num[0]

for i in range(0,4):
    if num[i] < num[i+1]:
        maior = num[i+1]
        

print (maior)
'''
'''
#8
print("Digite 5 Numeros:")
a = float(input("1: "))
b = float(input("2: "))
c = float(input("3: "))
d = float(input("4: "))
e = float(input("5: "))

soma = a + b + c + d + e

media = soma/5

print(soma)
print(media)
'''

'''
#9

for i in range(1,51):
    if i % 2 != 0:
        print(i)
        
'''

'''
#10

x = int(input("digite um numero: "))
y = int(input("digite um numero: "))

if x > y:
    z = x
    x = y
    y = z
    
for i in range (x+1, y):
    print(i)
'''

'''
#11
x = int(input("digite um numero: "))
y = int(input("digite um numero: "))
soma = 0

if x > y:
    z = x
    x = y
    y = z
    
for i in range (x+1, y):
    soma = soma + i
    
print(soma)
'''

'''
#12
x = int(input("digite um numero: "))

for i in range(1,11):
    mult = x * i
    print("{} X {} = {}".format(x, i, mult))
    
'''

'''
#13
x = int(input("digite um numero: "))
y = int(input("digite o expoente: "))
z = 1

for i in range(0,y):
    z = z * x

print(z)

'''

'''
#14

lista = []
par = 0
impar = 0

for i in range(0,10):
    x = int(input("digite um numero: "))
    lista.append(x)

for num in lista:
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
        
print("numero pares: ", par)
print("numero impares: ", impar)
'''

'''
#15
n = int(input("digite o termo: "))
atual = 1
anterior = 0
x = 0

for i in range(0,n):
    x = atual
    atual = atual + anterior
    anterior = x
    print(atual)
'''

'''
#16
cont = 0
atual = 0
proximo = 1

while cont < 500:
    cont += 1
    print(atual)
    z = atual
    atual = proximo
    proximo = atual + z
'''

'''
#17
x = int(input("Digite o numero do fatorial: "))
y = 1

for i in range (x, 0, -1):
    y = y * i
    
print (y)
'''

'''
#18

lista = []


for i in range(0,10):
    x = int(input("digite um numero: "))
    lista.append(x)

maior = lista[0]
menor = lista[0]
soma = 0

for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
        
    soma = soma + num
    
print("Maior número:", maior)
print("Menor número:", menor)
print("Soma números:", soma)

'''

'''
#19

lista = []


for i in range(0,10):
    x = int(input("digite um numero: "))
    while x <= 0 or x >= 1000:
        x = int(input("digite um numero: "))
    lista.append(x)

maior = lista[0]
menor = lista[0]
soma = 0

for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
        
    soma = soma + num
    
print("Maior número:", maior)
print("Menor número:", menor)
print("Soma números:", soma)
'''


'''
#20
loop = "S"

while loop == "S":
    x = int(input("Digite o numero do fatorial: "))
    while x <= 0 or x > 16:
        x = int(input("Digite o numero do fatorial: "))
    y = 1

    for i in range (x, 0, -1):
        y = y * i
    
    print (y)
    
    loop = str(input("Deseja continuar? (S/N) "))
    
'''

'''
#21

x = int(input("Digite um numero: "))
primo = True


for i in range (2,x):
    if x % i == 0:
        primo = False
        
if primo == True:
    print("É Primo")
    
else:
    print("Não é Primo")

'''

'''
#22
x = int(input("Digite um numero: "))
primo = True
divisores = []

for i in range (2,x):
    if x % i == 0:
        primo = False
        divisores.append(i)
        
if primo == True:
    print("É Primo")
    
else:
    print("Não é Primo")
    print (divisores)
'''

'''
#23

x = int(input("Digite um numero: "))
primos = []
divisoes = 0

for i in range (2,x):
    primo = True
    for j in range (2, i):
        if primo == False:
            break
        divisoes += 1
        if i % j == 0:
            primo = False
            
    
    
    if primo == True:
        primos.append(i)
        
print(primos)        
print(divisoes)

'''

'''
#24

n = int(input("Digite o numero de notas: "))
soma = 0


for i in range (0,n):
    soma =  soma + int(input("Digite a nota {}: ".format(i+1)))


media = soma / n

print(media)
'''

'''
#25

n = int(input("Digite o numero de pessoas: "))
total = 0

for i in range (0,n):
    total = total + int(input("digite a idade da pessoa {}: ".format(i+1)))
    
    
media = total/n

if media >= 0 and media <= 25:
    print("A turma é jovem")
elif media > 25 and media <= 60:
    print("A turma é adulta")
elif media > 60:
    print("A turma é idosa")
'''