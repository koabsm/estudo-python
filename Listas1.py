"""
Listas em Python 
fatiamento 
append
"""


lista = ['A', 'Bacana', 'Casa', '10.4', 'Cabeca']

print (lista[4])
print (lista[0:3])
print (lista[0:])


l1 = [1,2,3,4]
l2 = [3,4,5,6]
l3 = [l1+l2] # concatena 

print (l1)
print (l2)
print (l3)


l1.extend(l2)
print(l1)
print(l2)

l1.append('chico') #append string toda inserindo novo valor (insere a string dentro de um  indice)

l1.insert(-1, 'carro') #insere no ultimo indice 


l1.extend('betina') #insere caractere a caractere (betina sao 6 indices insere 6 indices) na l1 (ja concatenada)
print (l1)



l1.pop(4)
print (l1)


print (l2)
print ('maior valor da lista: ', max(l2))
print ('menor valor da lista: ', min(l2))
 ##',  menor valor da lista 'min(l2)',)
#('Caracteres mais: ',nome_formatado2)

print ('Remove indice na posicao de 0 a 3')
del(l2[0:3])
print (l2)