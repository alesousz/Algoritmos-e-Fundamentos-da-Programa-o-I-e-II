#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
numero = int(input('Digite um numero: '))
razao = int(input('Digite a razao: '))
final = numero + (11 - 1)*razao
for c in range(numero, final,razao):
    print(c, end=" > ")
print('ACABOU')