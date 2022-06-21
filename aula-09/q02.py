valor1 = int(input('primeiro valor: '))
valor2 = int(input('segundo valor: '))
valor3 = int(input('terceiro valor: '))
if (valor1 > valor2) and (valor1 > valor3) and (valor2 > valor3):
    print(f'valor em decrescente {valor1} , {valor2} , {valor3}')
elif (valor1 > valor2) and (valor1 > valor3) and (valor3 > valor2):
    print(f'valor em decrescente {valor1} , {valor3} , {valor2}')
elif (valor2 > valor1) and (valor2 > valor3) and (valor1 > valor3):
    print(f'valor em decrescente {valor2} , {valor1} , {valor3}')
elif (valor2 > valor1) and (valor2 > valor3) and (valor3 > valor1):
    print(f'valor em decrescente {valor2} . {valor3} , {valor1}')
elif (valor3 > valor1) and (valor3 > valor2) and ( valor1 > valor2):
    print(f'valor em decrescente {valor3} , {valor2} , {valor1}')
else:
    print(f'valor em decrescente {valor3} , {valor1} , {valor2}')
