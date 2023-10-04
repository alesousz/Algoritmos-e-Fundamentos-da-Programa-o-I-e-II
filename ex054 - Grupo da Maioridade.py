#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
cont = 0
cont2 = 0
for idade in range(0, 7):
    ano=int(input('Digite seu ano de nascimento: '))
    ano_atual = date.today().year
    idades = ano - ano_atual
    if abs(idades) > 17:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print(f'Existem {cont} maiores de idade')
print(f'Existem {cont2} menores de idade')