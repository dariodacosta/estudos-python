from math import sin
# from math import abs

numero1=float(input('primeiro: '))
numero2=float(input('segundo: '))
print('a soma dos' , numero1+numero2)
print('o produto do primeiro pelo quadrado do segundo' , numero1/(numero2*numero2))
print('o quadrado do primeiro' , (numero1*numero1))
print('a raiz quadrada da soma dos quadrados' , ((numero1*numero1)+(numero2*numero2)**0.5))
print(sin(numero1 - numero2))
print(abs(numero1))