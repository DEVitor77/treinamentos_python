n_1 = float(input('Entre com a primeira nota: '))
n_2 = float(input('Entre com a segunda nota: '))
media = (n_1 + n_2) / 2
print( 'A média do Aluno é de: ', media)


n_1 = float(input('Entre com a primeira nota: '))
n_2 = float(input('Entre com a segunda nota: '))
trabalho = float(input('Entre com a nota do trabalho: '))
#calculo da media ponderada
media = (n_1 * 1.5 + n_2 *2.5 + trabalho * 1.0) / (1.5 + 2.5* 1.)
print( 'A média do Aluno é de: ', media)

