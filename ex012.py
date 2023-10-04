#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto=float(input('Qual o valor do produto desejado ?'))
desconto=float(input('Quanto é o desconto?'))
valor_desconto=(produto*desconto)/100
preço_desconto=produto-valor_desconto
print(f'O novo valor do produto com desconto é {preço_desconto} reais')