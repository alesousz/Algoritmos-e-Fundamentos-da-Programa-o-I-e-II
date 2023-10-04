#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
lista = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
print('Bem-vindo ao Jogo!')
print('[0] - Pedra\n[1] - Papel\n[2] - Tesoura')
escolha=int(input('Escolha entre Pedra, Papel e Tesoura: '))
if escolha == 0:
    pc=randint(0, 2)
    if pc == 2:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('EU ESCOLHI TESOURA, VOCÊ GANHOU DESSA VEZ!')
    elif pc == 1:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('EU ESCOLHI PAPEL, DESSA VEZ EU VENCI!')
    elif pc == 0:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('EU ESCOLHI PEDRA, DESSA VEZ EMPATAMOS!')
elif escolha == 1:

    if pc == 2:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('EU ESCOLHI TESOURA, DESSA VEZ EU VENCI!')
    elif pc == 1:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('EU ESCOLHI PAPEL, DESSA VEZ EMPATAMOS!')
    elif pc == 0:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('EU ESCOLHI PEDRA, VOCÊ GANHOU DESSA VEZ!')
elif escolha == 2:

    if pc == 0:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('EU ESCOLHI PEDRA, DESSA VEZ EU VENCI!')
    elif pc == 1:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('EU ESCOLHI PAPEL, VOCÊ GANHOU DESSA VEZ!')
    elif pc == 2:
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('EU ESCOLHI TESOURA, DESSA VEZ EMPATAMOS!')
'''item = ('Pedra', 'Papel', 'Tesoura' )'''
'''computador = randint(0, 2)'''
#SE EU QUERO QUE O COMPUTADOR LEIA A PALAVRA E NÃO O NUMERO EU FAÇO : itens[computador], assim quando o computador escolher entre 0,1 e 2, ele vai ler o 0, 1 e 2 que está no item, pedra é 0 e assim por diante