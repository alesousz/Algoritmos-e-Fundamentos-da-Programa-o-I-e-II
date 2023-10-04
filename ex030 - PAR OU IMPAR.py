#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um numero: '))
resultado = numero % 2
if resultado == 0:
    print(f'{numero} é um numero PAR')
else:
    print(f'{numero} é um numero IMPAR')
