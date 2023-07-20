n = int(input("Digite um número natural: "))
contador = 0
numero = 0

while contador < n:
    if numero % 2 == 0:
        print(numero)
        contador += 1
    numero += 1
    