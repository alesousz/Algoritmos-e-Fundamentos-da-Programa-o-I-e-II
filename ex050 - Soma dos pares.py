#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
c = 0
for n in range(1, 7):
    p1 = int(input('Digite um numero: '))
    if p1%2 == 0:
        s = p1 + s
        c = c + 1
print(f'A soma dos {c} valores pares informados é de {s}')
