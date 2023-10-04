#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome=input('Qual é seu nome ?').strip()
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')

#'Curso' in frase > EXISTE A PALAVRA CURSO EM FRASE > RETORNA TRUE OU FALSE