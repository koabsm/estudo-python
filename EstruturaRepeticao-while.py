"""
Exemplo de while infinito 
"""

# Exemplo de while simples 
"""
print ('Exemplo while 01')
x = 0
while x < 10: 
    print (x)
    x = x + 1
print ('Indica fim do loop')
"""
print ('Exemplo while 02')
 
"""
x = 0 
while x < 10: 
   if x == 3: # condicao para manutencao do loop 
      x = x + 1
      #continue # --> continua o laco 
      break # quebra o laco 
   print('Debug', x)
   x = x + 1 
print ('Acabou ')

"""
"""
x = 0 # coluna 
y = 0 # linha 

print ('Exemplo 02 \n ')
while x < 10: 
    while y < 5: 
     print ('Coluna', x)
     print ('Linha', y)
     print (f'X vale {x} e Y valor {y}') #exemplo professor 
     x += 1 #x = x +1
     y += 1 
print ('acabou exemplo02 \n')
"""

#loop infinito 

while True:   #loop infinito 

     print ()
     sair = input('Deseja usar a calculadora [s]im ou [n]ao: ')
     num_1 = input ('Digite um numero:  ')
     num_2 = input ('Digite segundo numero: ')
     operador = input ('Digite um operador + - * / ')
     
     if sair == 'n': #S --> é a string 
        break
     if not num_1.isnumeric() or not num_2.isnumeric():
         print('Voce precisa digitar um numero')
         continue
     num_1 = int(num_1)
     num_2 = int(num_2)
     if operador == '+':
        print (num_1 + num_2)
     elif operador == '*':
        print (num_1 * num_2)
     elif operador == '-':
        print (num_1 - num_2)
     elif operador == '/':
        print (num_1 / num_2)
     else: 
        print ('operador invalido')
