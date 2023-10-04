#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = int(input('Digite um valor em metros: '))
centimetros = int(metros*100)
milimetros = int(metros*1000)
print(f'A conversão de {metros} metros para centimentros é de {centimetros}\nA conversão de {metros} metros para milimetros é de {milimetros}')