#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
ano = int(input('Digite um ano ou tecle 0 para analisar o ano atual: '))
bissexto = ano % 4 and ano % 100 != 0 or ano % 400 == 0
if bissexto==0:
    print(f'O ano de {ano} é um ano Bissexto')
elif ano == 0:
    ano=datetime.date.today().year
    resultado_ano = ano % 4 and ano % 100 != 0 or ano % 400 == 0 #FORMULA DO ANO BISSEXTO
    if resultado_ano == 0:
        print(f'O ano de {ano} é BISSEXTO')
    else:
        print(f'O ano {ano} NÃO É BISSEXTO')
else:
    print(f'O ano de {ano} não é um ano Bissexto')