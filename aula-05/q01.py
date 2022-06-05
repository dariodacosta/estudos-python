# 1. As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
# compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
# escreva o custo total da compra.

quantidade1 = 7
quantidade2 = 12
preco1 = 1.30
preco2 = 1.0
total1 = preco1*quantidade1
total2 = preco2*quantidade2
if total1>total2
    print('O valor das maçãs com menos: ' , total1)
if total2>total1
    print('O valor das maçãs com doze: ' , total2)