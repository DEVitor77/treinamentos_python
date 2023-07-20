'''	Refaça	o	programa	anterior	de	modo	que	todo	
produto	inserido	pelo	usuário	seja	numerado	sequencialmente,	
iniciando	em	1,	e	que	o	programa	exiba	a	menagem	“Compra	do	
ítem X negada!”,	após	a	leitura	do	item	que	extrapolar	o	valor	do	
crédito,	onde	X é	o	número	do	item.	Acrescente	as	instruções	
necessárias	para	ao	final	exibir	a	quantidade	de	itens	que	
puderam	ser	comprados'''

credito = float(input('Seu crédito:  ')) 
total = 0
item = 1


while True:
    preco = float(input(f'Preço do item {item}: '))
    if preco > credito:
        print(f'Compra do item {item} negada!')
    else:
        total += preco
        credito -= preco
    item += 1
    if credito <= 0:
        break


print(f'Quantidade de itens comprados: {item-1}')
print(f'Total de compra: R$ {total:.2f}')

print(f'Crédito restante: R$ {credito:.2f}') 


'''No código acima, utilizamos a condição if preco > credito dentro do loop para verificar se o preço do item
é maior que o crédito disponível. Nesse caso, exibimos a mensagem "Compra do item X negada!", onde X é o
número do item, sem utilizar a instrução break.


Em vez disso, utilizamos um loop infinito com a instrução while True e uma condição de saída if credito <= 0,
 que verifica se o crédito disponível acabou. Dessa forma, o loop é interrompido quando não há mais crédito
 para comprar novos itens.


Ao final do loop, exibimos na tela a quantidade de itens comprados, o total gasto com as compras e o crédito
restante.'''