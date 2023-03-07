num1 = input('Digite um numero')
num2 = input('Digite outro numero: ')

# builtin isnumero isfigit isdecimal 
# link: https://docs.python.org/3.6/library/stdtypes.html?highlight=isdigit
try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
except: 
    print('Nao pude converter os numeros para realizar contas. ')
    