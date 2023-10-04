#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario, com 15% de aumento.
salario=float(input('Digite o valor do seu salario? '))
aumento=float(input('Quanto é o aumento oferecido? '))
salario_=float(salario*aumento)/100
salario_aumento=float(salario_+salario)
print(f'O valor do seu salario com um aumento de {aumento}% é de {salario_aumento}')