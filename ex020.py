#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1=input('Digite o Nome do Aluno: ')
a2=input('Digite o Nome do Aluno: ')
a3=input('Digite o Nome do Aluno: ')
a4=input('Digite o Nome do Aluno: ')
alunos={a1, a2, a3, a4}
print(f'A ordem de apresentação dos alunos sera: {random.sample(alunos, 4)}')