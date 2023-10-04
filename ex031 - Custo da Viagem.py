#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
viagem=float(input('Qual a distancia em Km que você pretende viajar? '))
promoção=(viagem*0.50)
viagem_normal=(viagem*0.45)
if viagem <= 200:
    print(f'A sua viagem vai custar R${promoção:.2f}')
else:
    print(f'Sua viagem vai custar R${viagem_normal:.2f} ')