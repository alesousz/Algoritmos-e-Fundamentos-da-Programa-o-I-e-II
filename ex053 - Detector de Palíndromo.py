#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ').strip().upper()
for i in frase:
    print(i, end='')
    contrario=frase[::-1]
print(F' ao contrario é {contrario}')
if contrario==frase:
    print('É UM PALINDROMO')
else:
    print('NÃO É UM PALINDROMO')
