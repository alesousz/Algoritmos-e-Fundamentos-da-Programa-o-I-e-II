#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
tuplas = (int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),
          int(input('Digite um numero: ')))
print(f'Os valores informados foram: {tuplas}')

#A
print(f'O numero 9 apareceu {tuplas.count(9)}')

#B
if 3 in tuplas:
    print(f'A posição do numero 3 é a {tuplas.index(3)}°')
else:
    print(f'O numero 3 não apareceu entre os numeros digitados')

#C
print('Os numero pares digitados foram:', end=' ')
for valor in tuplas:
    if valor % 2 == 0:
        print(f'{valor}', end=' ')


