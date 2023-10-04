#Exercício Python 026 - Primeira e última ocorrência de uma string: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').strip()
inicio_frase=frase.upper().find("A")
final_frase=frase.upper().rfind("A")
print(f'A letra A aparece {frase.upper().count("A")} vezes na frase {frase}')
print(f'A letra A aparece pela primeira vez na posição: {inicio_frase+1}')
print(f'A letra A apareceu pela ultima vez na posição: {final_frase+1} ')


#FRASE.COUNT('o') > VAI ME CONTAR QUANTAS VEZES EXISTE A LETRA O NA FRASE
#FRASE.FIND('deo') > QUANTAS VEZES ENCONTROU deo na string > MOSTRANDO TBM ONDE É QUE ISSO COMEÇA >> RFIND P/ REALIZAR A OPERAÇÃO AO CONTRARIO