#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
peso = float(input('Digite o peso em Kg: '))
altura = float(input('Digite a altura em metros: '))
imc = peso / (altura*altura)
if imc <= 18.5:
    print(f'Seu IMC é de {imc:.1f}, você está Abaixo do peso')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.1f}, você está no Peso Ideal')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.1f}, você está com Sobrepeso')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.1f}, você está com Obesidade')
else:
    print(f'Seu IMC é de {imc:.1f}, você está com Obesidade morbida')
