#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Qual seu ano de nascimento?'))
ano_atual = date.today().year
idade = abs(ano-ano_atual)
tempo=abs(idade)-18

print('''Qual o seu sexo?
[1] - Masculino
[2] - Feminino ''')
sexo=int(input('Opção: '))

if sexo == 1:
    if idade < 18:
        print(f'Você tem {abs(idade)} anos. Ainda não está na hora de se alistar, porém em {(ano_atual - tempo)} daqui a {abs(tempo)} anos chegara sua vez!')

    elif idade > 18:
        print(f'Você tem {abs(idade)} anos. Seu tempo de alistamento ocorreu em {(ano_atual - tempo)} há {abs(tempo)} anos. Caso não tenha se alistado se dirija a uma junta militar IMEDIATAMENTE.')

    else:
        print(f'Você tem {abs(idade)} anos. Está na hora de realizar seu alistamento pelo site: https://alistamento.eb.mil.br/ ')
elif sexo==2:
    print('O alistamento militar obrigatorio so é reservado para o sexo masculino')