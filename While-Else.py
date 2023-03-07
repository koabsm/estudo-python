"""
While / Else 
"""

contador = 1 
acumulador = 1 

while contador <=10: 
    print(contador,acumulador)
    if contador > 5: 
         break # indica para parar no 6 while - e vai direto pro print isso sera executado - 
    acumulador = acumulador + contador
    contador += 1 
else: # para aqui so a condicao do while contador <= 10 for verdadeira 
    print ('Cheguei no else - condicao de falso')
print('Isso sera executado')