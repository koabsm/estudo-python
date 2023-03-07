"""
Variaveis
"""

#Exemplo 01  utilizando type 

nome = 'Luiz'
print (nome, type(nome))


#Uso dinamico da varivel 

nome = 'Betina'
idade = 12 # int 
peso = 24.588 #float  
peso_ruim = peso >= 15
Data_e = True 
idade_atencao = idade > 10

print('Nome do dog:', nome)
print('Idade do dog:', idade)
print('Peso do dog:', peso)
print('Peso Ruim:', peso_ruim)
print('######')
#print('Nome:', nome, 'Idade:', idade) 
print('Nome:', nome, 'Idade:', idade, 'Peso Canino:', peso, 'Peso Ruim:', peso_ruim, 'Atencao com a idade:', idade_atencao)  #'Idade:' idade)  
#, peso, 'O peso do canino esta:' peso_ruim, 'Esta idade exige:' idade_atencao)
#print(nome, idade, peso, 'O peso do canino esta:' peso_ruim, 'Esta idade exige:' idade_atencao)
# Usando F
print ('Modo sem formatacao')
print('Nome:', nome, 'Idade:', idade)
print ('Modo com formatacao \n')
print(f' Nome:{nome}\n  Idade:{idade} \n  Peso: {peso:.1f}')
