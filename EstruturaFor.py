"""
for in em Python
Iterando string com for 
Funcao range (start=-, stop, step=1)

"""



texto =  'Python'
nova_string = ''
print ('usando while ')
c = 0 
while c < len(texto): # ele criou um condicional inteligente baseado no tamanho do texto / string 
    print(texto[c])
    c += 1

print ('usando for ')

for letra in texto: 
     print (letra)


print ('usando for 2 ')

for n, letra in enumerate(texto): #enumerate - inumera cada loop
     print (n, letra)

print ('\n Usando FOR - LETRAS  3 \n ')

for letra in texto: #enumerate - inumera cada loop
     if letra == 't': 
        nova_string = nova_string + letra.upper()
     elif letra == 'h': 
         nova_string += letra.upper() 
     else: 
         nova_string += letra
     print (nova_string) 

print ('\n Usando FOR 3 \n   ')

for numero in range(10):
    print (numero)

print ('Usando FOR 4 \n ')
for n in range(3,10, 1): # comeca no 3 termina no 10 e vai em 1 
   print (n)

print ('\n Usando FOR 5 \n   ')

for n in range(10):
    if n % 2 == 0: # multiplo de 8 
        print (n) 