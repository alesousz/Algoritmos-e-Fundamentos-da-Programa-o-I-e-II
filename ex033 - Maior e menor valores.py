# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1: float = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))
if n1 > n2 > n3:
    print(f'O {n1} é o maior')
    print(f'O {n3} é o menor')
if n1 > n2 and n2 < n3 and n1 > n3:
    print(f'O {n1} é o maior')
    print(f'O {n2} é o menor')
if n2 > n1 > n3:
    print(f'O {n2} é o maior')
    print(f'O {n3} é o menor')
if n2 > n1 and n1 < n3 and n2 > n3:
    print(f'O {n2} é maior')
    print(f'O {n1} é o menor')
if n3 > n1 > n2:
    print(f'O {n3} é o maior')
    print(f'O {n2} é o menor')
if n3 > n1 and n1 < n2 and n3 > n2:
    print(f'O {n3} é o maior')
    print(f"O {n1} é o menor")
