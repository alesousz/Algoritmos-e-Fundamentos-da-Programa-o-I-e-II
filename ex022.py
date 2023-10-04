#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo sem considerar espaços.
#Quantas letras tem o primeiro nome. print(f'{str.replace(nome)}')
from re import split

nome=input('Digite seu nome completo: ')
print(f'Seu nome completo com letras minusculas: {str.lower(nome)}\nSeu nome completo com letras maiusculas: {str.upper(nome)}')
print(f'O total de letras em seu nome sem considerar os espaços: {len(nome.replace(" ",""))}')
print(f'O total de letras em seu primeiro nome: {len(nome.split()[0])}')


