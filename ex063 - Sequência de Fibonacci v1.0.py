#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
#N primeiros elementos de uma Sequência de Fibonacci.
vezes = int(input('Digite a quantidade de termos: '))
cont = 0
Fn = 0
Fn2 = 1
while cont < vezes:
    print(f'{Fn}', end=' ')
    Fn3 = Fn + Fn2
    Fn = Fn2
    Fn2 = Fn3
    cont += 1
#um atualiza sobre o outro! É BOM LEMBRAR DISSO SEMPRE