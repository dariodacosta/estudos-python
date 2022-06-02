# Algoritmo para calcular quanto se vai pagar no frete de um determinado produto, sendo
# que a empresa cobra 1.50 o km e taxa de envio de R$ 9,00.
km = float(input('Cada km 1.50: '))
taxa = float(input('Taxa de R$9,00: '))
valor_do_frete = 9 + km * taxa
print('O valor de envio ficara: ', (9 + km * taxa))