#Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
d = float(input('Quantos reais você tem na carteira? R$'))
conv =float(d/3.27)
print(f'Com R${d:.2f} reais é possivel comprar U${conv:.2f} dolares')