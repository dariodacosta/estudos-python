# Algoritmo para calcular quanto se vai pagar no frete de um determinado produto, sendo
# que a empresa cobra 1.50 o km e taxa de envio de R$ 9,00.
TAXA = 9
PRECO_KM = 1.50
km = float(input('quantos km: '))
valor_do_frete = TAXA + km * PRECO_KM
print('O valor de envio ficara: ', valor_do_frete)