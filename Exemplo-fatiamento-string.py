""" 
Exemplo de uso for / matriz
Indices e fatiamento de string em python 

"""

# 2:12 / 5:36 / 7:38 / 8:13 / 8:48 / 9:39 / 10:17 / 11:48 / 12:20 / 14 


# indice positivos [0123456678] 
texto =             'Python s2'
# indice negativo -[9876543210] 

url = 'www.google.com.br/'
print (texto)
print (texto[0]) #primeiro caractere 
print (texto[-1]) # ultimo caractere 
print (texto[3])
print (texto[2])
print (texto[2:6]) # va do 2 ate 6 
print (texto[6:])
print (texto[-3])
print (texto[-9:-3])
print (texto[0:5:2]) #comece no caractere 0 e va ate o 5(6) e pule em 2 em 2 
print (texto[0:]) # indica pro python pular em 1 em 1 
print (len(texto)) # string tem indice e quantos caracteres elas tem 

print ( url[:-1]) # print sem o barra ultimo caracter - pega ultima caractere 
