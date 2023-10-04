#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import choice
from time import sleep
print('Bem-vindo ! Vou pensar em um numero e você tenta adivinhar ta bem?')
lista=[0, 1, 2, 3, 5]
pense=choice(lista)
jogo=int(input('Adivinhe o numero que eu pensei!'))
print('PROCESSANDO...')
sleep(3)
if jogo==pense:
    print('Parabens! Você acertou!')
else:
    print('Poxa! Você errou, tente novamente!')
    print(f'Eu pensei no numero {pense} e não no {jogo}')