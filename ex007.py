#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
nome = input('Qual é o nome do aluno? ')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2)/2
print(f'A media das notas de {nome} é {media:.2f} ')