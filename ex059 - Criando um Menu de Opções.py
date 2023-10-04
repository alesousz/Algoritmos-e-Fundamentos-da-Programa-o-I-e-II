#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
import math
print('Bem-vindo a calculadora 2.0v')
lista = []
for i in range(0, 2):
    numero = float(input('Digite um numero: '))
    lista.append(numero)
opçao = 0
while opçao != 5:
    print('Escolha uma operação:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair  ')
    opçao = int(input('Digite uma opção: '))
    if opçao == 1:
        soma = sum(lista)
        print(f'A soma dos numeros é {soma}')
    
    elif opçao == 2:
        produto = math.prod(lista)
        print(produto)

    elif opçao == 3:
        maior = max(lista)
        print(f'O maior valor é o {maior}')

    elif opçao == 4:
        for i in range(2):
            numero2=float(input('Digite os novos numeros: '))
            lista[i] = numero2
        print('Numeros adicionados!')


    if opçao == 5:
        print('Acabou')
