# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular
tupla = ('Mesa', 189.60,
         'Cadeira', 38.50,
         'Talheres', 15.90,
         'Panelas', 79.40,
         'Toalhas',55.30,
         'SEXO', 350)
print('-' * 40)
print('          PROMOÇÃO DA SEMANA   ')
print('-' * 40)
for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30}', end='')
    else:
        print(f'R${tupla[i]:>7.2f}')
print('-' * 40)