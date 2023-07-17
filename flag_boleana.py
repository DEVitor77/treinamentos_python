total = 0
quero_comprar = True

while quero_comprar:
    preco = float(input('preço: '))
    total = total + preco
    opcao = input(input('continuar comprando (s/n)? '))
    if opcao  != 's':
        quero_comprar = False

print(f'Total da compra: R$ {total:.2f}')