morangos = int(input('quantidade de morango: '))
macas = int(input('quantidade de macas: '))
preco_morango = float(input('preco do morango: '))
preco_maca = float(input('preco da maca: '))
preco_morango1 = morangos * 2.50
preco_morango2 = morangos * 2.20
preco_maca1 = macas * 1.80
preco_maca2 = macas * 1.50

if morangos > 5:
    preco_maca <= preco_morango1
    print('QUANTIDADE MORANGOS E O VALOR: ')
else:
    preco_maca <= preco_morango2
    print('QUANTIDADE MORANGOS E O VALOR: ')
if macas > 5:
    preco_maca <= preco_maca1
    print('QUANTIDADE MACAS E O VALOR: ')   
else:
    preco_maca <= preco_maca2
    print('QUANTIDADE MACAS E O VALOR: ')     
