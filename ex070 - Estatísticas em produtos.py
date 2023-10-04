#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
gastototal= maisdemil =  0
maisbarato = float('inf')
nomedoproduto = ''
print('LOJA SUPER BARATÃO')
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$'))
    gastototal += preço

    if preço > 1000:
        maisdemil += 1

    if preço < maisbarato:
        maisbarato = preço
        nomedoproduto = produto

    pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while pergunta not in ['S', 'N']:
        pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if pergunta == 'N':
        break

print(f'O total da compro foi R${gastototal}')
print(f'Temos {maisdemil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomedoproduto} que custa {maisbarato}')