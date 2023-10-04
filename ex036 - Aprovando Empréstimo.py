#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Qual o valor da casa?'))
salario = float(input('Qual o salario do comprador?'))
tempo = int(input('Em quantos anos pretende pagar?'))
meses = tempo*12
valor_prestações = valor/meses
porcentagem = (salario*30)/100
print(f'Para pagar uma casa de R${valor:.2f} em {tempo} anos, o valor da prestação será de R${valor_prestações:.2f}')
if valor_prestações > porcentagem:
    print(f'Emprestimo recusado, suas prestações no valor de R${valor_prestações:.2f} excedem 30%({porcentagem}) do salario de R${salario}')
else:
    print(f'Emprestimo APROVADO! Suas prestações no valor de R${valor_prestações:.2f} não exdecem 30%({porcentagem}) do seu salario')
