#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano  - ano_atual
if abs(idade) <= 9:
    print(f'O atleta com {abs(idade)} anos está na categoria MIRIM')
elif 14 >= abs(idade) > 9:
    print(f'O atleta com {abs(idade)} anos está na categoria INFANTIL')
elif 19 >= abs(idade) > 14:
    print(f'O atleta com {abs(idade)} anos está na categoria JUNIOR')
elif 25 >= abs(idade) > 19:
    print(f'O atleta com {abs(idade)} anos está na categoria de SENIOR')
elif abs(idade) > 25:
    print(f'O atleta com {abs(idade)} anos está na categoria de MASTER')
