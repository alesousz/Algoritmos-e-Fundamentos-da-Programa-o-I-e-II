# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import choice
from time import sleep
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Bem vindo ao Jogo de Adivinha!')

contador = 0
pense = choice(lista)
while True:
    contador = contador + 1
    pessoa = int(input('Qual o seu palpite: '))
    print('pensando...')
    sleep(2)
    if pessoa == pense:
        print(f'Você adivinhou! Eu pensei realmente no numero {pessoa}')
        break
    elif pessoa > pense:
        print(f'Menos...')
    elif pessoa < pense:
        print('Mais...')

print(f'Você tentou {contador} vezes para acertar!')



