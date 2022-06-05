# Escreva um programa que leia o valor de 3 ângulos de um triângulo
# e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
# Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
# Triângulo Obtusângulo: possui um ângulo obtuso.(maior que 90º)
# Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)
a = 30
b = 40
c = 20
if (a + b + c):
    print('RETANGULO')
elif (a > 90) or (b > 90) or (c > 90):
    print('OBTUSANGULO')
else:
    print('ACUTANGULO')        