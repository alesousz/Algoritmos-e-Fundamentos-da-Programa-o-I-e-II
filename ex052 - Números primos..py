#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um numero: '))
cont = 0
for c in range(1, numero+1):
    print(c, end=' > ')
    if numero % c == 0:
        cont = cont + 1
#O CONT ESTÁ CONTANDO QUANTOS NUMEROS DENTRO DO FOR DIVIDIDOS PELA VARIAVEL NUMERO TEM RESTO 0
print(f'\nO numero {numero} foi divisivel por {cont} numeros')

if cont == 2:
    print(f'O numero {numero} é um numero primo!')
else:
    print(f'O numero {numero} não é um numero primo!')












