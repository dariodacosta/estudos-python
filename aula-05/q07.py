# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:
# Triângulo Equilátero: possui os 3 lados iguais.
# Triângulo Isóscele: possui 2 lados iguais.
# Triângulo Escaleno: possui 3 lados diferentes.
from ctypes.wintypes import INT


a = int(input('LADO 1: '))
b = int(input('LADO 2: '))
c = int(input('LADO 3: '))
if (a == b) and (a == c):
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')
else:
    print('Escaleno')