# Leia duas strings e efetua as trocas dos valores de forma que a variável A
# passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A.

a = int(input(' valor A: '))
b = int(input(' valor B: '))
c = a 
a = b
b = c
print(' A troca dos valores fica: ' , (a,b))