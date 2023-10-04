#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesos = []
for b in range(1, 6):
    peso = int(input(f'Digite o peso em Kg da {b}° pessoa: '))
    pesos.append(peso)
#USANDO O METODO APPEND, QUE ADICIONA OS VALORES INFORMADOS NO INPUT PESO, DENTRO DA LISTA VAZIA PESOS
menorpeso = min(pesos)
maiorpeso = max(pesos)
print(f'O menor peso é o {menorpeso}kg')
print(f'O maior peso é o {maiorpeso}kg')
#USANDO MIN E MAX PODEMOS ENCONTRAR O MAIOR E MENOR VALOR DENTRO DE UMA LISTA

#tentando usar enumerate para indicar a posição na lista, estudar mais essa fita
'''for posicao, peso in enumerate(pesos, 1):
    print(f'O menor peso é o {posicao}° pessoa, com {menorpeso}kg')
    print(f'O maior peso é o {posicao}° pessoa, com {maiorpeso}kg')
    break'''