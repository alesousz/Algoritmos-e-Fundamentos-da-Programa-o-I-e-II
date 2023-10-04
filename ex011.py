#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2m².
largura=float(input('Digite a largura da parede em m²: '))
altura=float(input('Digite a altura da parede em m²: '))
area=float(largura*altura)
tinta=float(area/2)
print(f'A area da sua parede é de {area:.2f}m²')
print(f'A quantidade de tinta necessaria para pintar a parede desejada é de {tinta:.2f}Litros')