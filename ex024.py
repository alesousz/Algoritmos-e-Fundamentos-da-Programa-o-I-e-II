#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
city=input('Digite o nome da sua cidade: ').strip()
print(f'{city.upper()[:5]=="SANTO"}')

#Na resolução do Guanabara ele fez diferente, utilizando duas funções strip (que remove os espaços) e upper (deixando tudo maiusculo)
#'Curso' in frase > EXISTE A PALAVRA CURSO EM FRASE > RETORNA TRUE OU FALSE