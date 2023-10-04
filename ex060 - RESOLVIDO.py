#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
numero = int(input('Digite um numero: '))
contador = 1
for i in range(1, numero+1):
    contador = contador * i
print(f'o resultado é {contador}')