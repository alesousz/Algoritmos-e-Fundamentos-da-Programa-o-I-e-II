# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome: '))
variavel_nome = nome.split()
print(f'Seu primeiro nome é {variavel_nome[0]}')
print(f'Seu ultimo nome é {variavel_nome[-1]}')

# FRASE.SPLIT() > A CADA ESPAÇO ELE SEPARA A STRING, E O QUE FICA DIVIDIDO SE TORNA 1,2,3 (DA PRA ENCAIXAR AI DENTRO De um [] PRA TIRAR UMA PALAVRA ESPECIFICA
#-1 no python busca a ultima string em uma lista, então se eu queria o primeiro eu uso 0 e o ultimo eu uso -1