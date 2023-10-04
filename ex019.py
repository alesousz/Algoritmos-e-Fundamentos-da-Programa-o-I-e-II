#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
aluno_1=(input('Nome do Aluno: '))
aluno_2=(input('Nome do Aluno: '))
aluno_3=(input('Nome do Aluno: '))
aluno_4=(input('Nome do Aluno: '))
lista=[aluno_1, aluno_2, aluno_3, aluno_4]
print(f'O aluno escolhido é {choice(lista)}')