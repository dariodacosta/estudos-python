nome = str(input('nome do produto: '))
quantidade = int(input('quantidade adquirida: '))
preco = float(input('preco unitario: '))
total = (quantidade*preco)
total_a_pagar1 = (total - 0.02)
total_a_pagar2 = (total - 0.03)
total_a_pagar3 = (total - 0.05)
if quantidade <= 5:
    print('O DESCONTO SERA DE 2%: ' , total_a_pagar1)
elif quantidade > 5 and quantidade <=10:
    print('O DESCONTO SERA DE 3%: ' , total_a_pagar2)
else:
    quantidade > 10
    print('O DESCONTO SERA DE 5%: ', total_a_pagar3)