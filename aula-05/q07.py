# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:
# Triângulo Equilátero: possui os 3 lados iguais.
# Triângulo Isóscele: possui 2 lados iguais.
# Triângulo Escaleno: possui 3 lados diferentes.
a = 2
b = 2
c = 2
if (a + b < c) or (a + c < b) or (b + c < a):
    print('medida dos triangulo')
elif (a == b) and (a == c):
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')
else:
    print('Escaleno')