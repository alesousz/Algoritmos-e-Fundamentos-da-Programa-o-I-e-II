#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
total = 0
for i in range(1, 501, 6):
    total += i
print(f'A soma dos valores é {total}')

c = 0
s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s = s + i
        c = c + 1
print(f'A soma de todos os {c} valores é {s}')

