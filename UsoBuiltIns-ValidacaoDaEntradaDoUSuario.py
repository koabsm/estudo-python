num1 = input('Digite um numero')
num2 = input('Digite outro numero: ')

# builtin isnumero isfigit isdecimal 
# link: https://docs.python.org/3.6/library/stdtypes.html?highlight=isdigit
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else: 
    print('Nao pude converter os numeros para realizar contas. ')
    