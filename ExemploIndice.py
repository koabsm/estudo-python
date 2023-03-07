
#Exemplo de Indice 

#       Indices 
#       0123456789.................33

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0 
nova_string = ''

#while contador < tamanho_frase: 
#  print(frase[contador], contador)
#   contador += 1

"""
while contador < tamanho_frase: 
   #print(frase[contador], contador)
   nova_string += frase[contador]
   contador += 1

   print(nova_string)

print('nova string:...........', nova_string)

"""

while contador < tamanho_frase: 
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R' #substitui r ->R na nova string 
        print('r', nova_string)
    else: 
        nova_string += letra 
        print('nao r', nova_string)
    contador += 1

print(nova_string)

