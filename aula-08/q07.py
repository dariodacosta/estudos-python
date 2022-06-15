lados = int(input('valor de lados: '))
perimetro = (lados + lados + lados)
area = (lados**2)
if lados == 3:
    print('IGUAL A TRIANGULO' , perimetro)
elif lados == 4:
    print('IGUAL A QUADRADO' , area)
elif lados == 5:
    print('IGUAL A PENTAGONO')
elif lados > 5:
    print('POLIGONO NAO INDENTIFICADO')    
else:
    print('NAO E UM POLIGONO')