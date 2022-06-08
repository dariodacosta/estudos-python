# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever
# uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o
# aluno é aprovado). Escrever também a média calculada.
nota_1a = float(input('nota: '))
nota_2a = float(input('nota: '))
nota_final = (nota_1a + nota_2a)/2

if nota_final >6:
    print('APROVADO')
else:
    print('REPROVADO')
       
