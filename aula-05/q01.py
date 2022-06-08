# 1. As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
# compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
# escreva o custo total da compra.

quantidade1 = int(input('Quantidade: '))
quantidade2 = float(input('Quantidade: '))
preco1 = 1
preco2 = 1.30
total1 = preco1*quantidade1
total2 = preco2*quantidade2
print('O valor das maçãs com menos: ' , total1)
print('O valor das maçãs com doze: ' , total2)