a = int(input('valor: '))
b = int(input('valor: '))
c = int(input('valor: '))
soma_dos_lados = (a + b + c)
if a <= ( c + b ) and b <= (a + c) and c <= (a + b):
    print('forma um triangulo' , soma_dos_lados)
else:   
    print('nao forma um triangulo' , soma_dos_lados)