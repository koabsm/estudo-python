"""
Lista em python
"""

l2 = list(range(1,10)) #Exemplo de uma lista criada do 1 ate o 10 = usando a funcao RANGE
print (l2)


l3 = list(range(0,110, 10)) #Exemplo de uma lista criada do 1 ate o 10, pulando de 10 em 10  = usando a funcao RANGE 
print (l3)

for valor in l3:
    print (valor)
    resultado = valor * 2
    print (resultado)

l4 = ['String', True, 10, -20.5]

for elem in l4: 
    print(f'O tipo de {type(elem)} é  {elem}')

 