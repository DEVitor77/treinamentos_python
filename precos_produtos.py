total = 0
preco = float(input('preco do item: '))

while preco != -1:
    total = total + preco
    preco = float(input('incluir outro preco: '))

print(f'O total da compra deu: R$ {total:.2f}')   