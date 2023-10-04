#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite seu salario: '))
if salario > 1250:
    aumento=(salario*10/100) + salario
    print(f'O salario com base no aumento de 10% passa a ser de R${aumento:.2f}')
if salario <= 1250:
    aumento=(salario*15/100) + salario
    print(f'O salario com base no aumento de 15% passa a ser de R${aumento:.2f}')