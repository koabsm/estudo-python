"""
Operadores relacionais 
"""

nome = input('Qual o seu nome?')
idade = input ('qual a sua idade ?')

idade = int(idade) 
idade_maior = 30
idade_menor = 20 
idade_limite = 18 
print ('######## CONDICIONAL 01 ######### \n')
if idade >= idade_limite: 
    print (f'{nome} pode pegar o emprestino')
else:
    print (f'{nome} NAO PODE pegar o emprestimo')

print ('######## CONDICIONAL 02 ######### \n')

if idade >= idade_menor and idade <= idade_maior: 
    print (f'{nome} pode pegar o emprestino')
else:
    print (f'{nome} NAO PODE pegar o emprestimo TA VELHO RAPAZINHO')