'''Podemos calcular o quociente da divisão inteira de x por y utilizando um loop while. A ideia 
é subtrair y de x quantas vezes for possível, até que o resultado se torne negativo. A quantidade de
 vezes que y foi subtraído de x é o quociente da divisão inteira de x por y.


Segue abaixo o código em Python que implementa essa lógica:'''

# Solicitando ao usuário os valores de x e y
x = int(input("Digite um número natural x: "))
y = int(input("Digite um número natural y: "))

# Calculando o quociente da divisão inteira de x por y
quociente = 0
while x >= y:
    x -= y
    quociente += 1

# Exibindo o resultado
print("O quociente da divisão inteira de", x, "por", y, "é", quociente)


'''Note que nesse código utilizamos a variável quociente para contar a quantidade de vezes que y foi 
subtraído de x.
 O loop while é executado enquanto x for maior ou igual a y, subtraindo y de x em cada iteração
 e incrementando o quociente.

Ao final do loop, o valor de quociente corresponde ao quociente da divisão inteira de x por y.'''