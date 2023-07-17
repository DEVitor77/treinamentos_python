credito = float(input('seu credito: ')) #variavel acumuladora
total = 0 #variavel acumuladora

preco = float(input('preço do item: '))
while credito >= preco:
    total = total + preco
    credito = credito - preco
    preco = float(input('preço  de mais um item: '))
    
print(f'total de compra: R$ {total:.2f}')    
print(f'credito restante: R$ {credito:.2f}')
