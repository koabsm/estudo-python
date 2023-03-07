"""
Formatacao de valores 
:s string
:f flutuante
:d inteiros 
:. (numero) f - quantidade casa decimais (float) 
: (Caractere) > ou < ou ^quantidade tipo - s , d ou f 
"""

print ('Exemplo 01 formatando float \n ')

num_1 = 10 
num_2 = 3
resultado = num_1 / num_2

print ('valor normal ', resultado)
print ('valor formatado {:.2f}'.format(resultado))

print ('Exemplo 02  formatando string \n')

nome = 'Bruno Steven'
print(f'{nome:s}\n ')

print ('Exemplo 03 Inserindo casa decimais ')

num_3 = 1 
print(f'{num_3:0>10}')

num_2 = 1150 
print(f'{num_2:0<10}')
print(f'{num_2:0<10.2f}\n')

print ('Exemplo 04 string preenchendo caractere ')

nome2 = 'Otavio Miranda'
print ( 50-len(nome2)/ 2 )
print (f'{nome2:#^50}\n')
print ('nao foi adicionado pq a string conta a partir do total de caracteres \n ')

print ('Exemplo 05 string preenchendo caractere \n  ')

nome_formatado2 = '{:@>14}'.format(nome2) 
print ('Carateres batem: ', nome_formatado2)
nome_formatado2 = '{:!>20}'.format(nome2) 
print ('Caracteres mais: ',nome_formatado2)

print ('Exemplo 06 Controle Maisculo e Minusculo \n  ')

nome4 = 'Betina'
print(nome4.lower()) 
print(nome4.upper()) 
print(nome4.title()) # primeira letras maisculas



