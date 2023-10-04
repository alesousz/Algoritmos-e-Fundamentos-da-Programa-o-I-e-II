#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
velocidade = float(input('Digite a velocidade do seu carro em Km/h: '))
custo = (80-velocidade)*7
if velocidade > 80:
    print(f'CUIDADE! Você ultrapassou a velocidade maxima de 80Km/h, sua multa é no valor de R${abs(custo)}')
else:
    print('Você está dentro do limite de velocidade! Continue assim!')

#abs para deixar o numero com o valor positivo
