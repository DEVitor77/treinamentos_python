numero = int(input('Digite um número natural maior ou igual a 2: '))
if numero >= 2:
    if numero % 2 == 0:
        print(numero - 1, numero + 2)
    else:
        print(numero - 2, numero + 1)
else:
    print('O número digitado é menor do que 2. Por favor, tente novamente.')
