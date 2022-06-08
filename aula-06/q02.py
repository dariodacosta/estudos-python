# ler tres valores (considere que nao serao informados valores iguais ) e escreva o maior deles
a = int(input('valor: '))
b = int(input('valor: '))
c = int(input('valor: '))
maior_valor = (a ,b, c)
if b > a and b > c and c > a:
    maior_valor = b
    print(maior_valor)
elif c > b and a > c and b > a:
    maior_valor = c 
    print(maior_valor)
elif a > b and c > a and c > b:
    maior_valor = a
    print(maior_valor)
else:
    maior_valor = a
    print(maior_valor)