"""
Exemplo de contagem de caracteres 
"""


usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres), type(usuario))

print(len(usuario))
print(usuario.__len__()) #nao server para numero e nem para boolean python -