#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
preço=float(input('Digite o valor das compras: '))
print('Qual será a forma de pagamento:\n[1] - à vista dinheiro/cheque: 10% de desconto\n[2] - à vista no cartão: 5% de descontol\n[3] - em até 2x no cartão: preço formal\n[4] - 3x ou mais no cartão: 20% de juros ')
desconto_avista = (preço*10/100) - preço
opção = int(input('Opção: '))

if opção == 1:
    print(f"O valor total a ser pago com o desconto de R${preço*10/100:.2f}  é de R${abs(desconto_avista):.2f}")

elif opção == 2:
        desconto_avista_cartao=(preço*5/100) - preço
        print(f'O valor total a ser pago com o desconto de R${preço*5/100:.2f}  é de R${abs(desconto_avista_cartao):.2f}')

elif opção == 3:
    vezes = int(input('Em quantas vezes: '))
    if vezes > 2:
        print('Operação incorreta')
    else:
        print(f'O valor de cada parcela será de R${preço/vezes:.2f}')

elif opção == 4:
    vezes=int(input('Quantas vezes no cartão?'))
    juros=preço + (preço*20/100)
    total=juros/vezes
    print(f'O valor a ser pago em {vezes}x é de R${total:.2f} por mês, com um valor total de {juros}')
else:
    print('Opção incorreta, tente novamente.')