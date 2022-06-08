a = int(input('valor: '))
b = int(input('valor: '))
c = int(input('valor: '))
maior_valor = (a, b, c)
segundo_maior = (a, b, c)
if b > a and b >c and a > c:
    maior_valor = b
    segundo_maior = a
    print(maior_valor , segundo_maior)    
elif c > b and c > a and b > a:
    maior_valor = c
    segundo_maior = b
    print(maior_valor , segundo_maior)    
elif a > b and a > c and c > b:
    maior_valor = a
    segundo_maior = c
    print(maior_valor , segundo_maior)
else:
    maior_valor = a
    segundo_maior = c
    print(maior_valor , segundo_maior)

