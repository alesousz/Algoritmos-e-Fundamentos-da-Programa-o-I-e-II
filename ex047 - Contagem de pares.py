#Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from time import sleep
for numeros in range(1, 51):
    par = numeros % 2
    if par == 0:
        print(f'{numeros};', end=" ")
        sleep(1)

print('ESSES SÃO OS NUMERO PARES DE 0 A 50')