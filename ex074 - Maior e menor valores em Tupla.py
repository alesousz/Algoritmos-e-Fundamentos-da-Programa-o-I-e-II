#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10) )
print(tupla)
maior = max(tupla)
print(f'O maior numero é {maior} ')
menor = min(tupla)
print(f'O menor numero é {menor}')