"""
Teste IF
"""

nome_bairro = input ("Entre com nome do seu bairro.....:\n ")

nome_bairro_1 = 'asanorte'
nome_bairro_2 = 'asasul' 
nome_bairro_3 = 'mangueral' 

if nome_bairro == nome_bairro_1:
   print (f'\n Nome do bairro que voce entrou {nome_bairro} bate com a primeira opcao {nome_bairro_1}')
elif nome_bairro == nome_bairro_2: 
   print (f'\n Nome do bairro que voce entrou {nome_bairro} bate com a primeira opcao {nome_bairro_2}')
elif nome_bairro == nome_bairro_3: 
   print (f'\n Nome do bairro que voce entrou {nome_bairro} bate com a primeira opcao {nome_bairro_3}')
else: 
   print ("\n Nao combinou")
