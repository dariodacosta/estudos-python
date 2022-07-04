empregado = str(input('codigo do empregado: '))
data_nc = int(input('data de nacimento : '))
data_add = int(input('ano de ingresso na empresa: '))
data_atual = int(input('ano atual na empresa: '))
tempo_empr = (data_add - data_atual)
idade = (data_nc - data_atual)

if (idade >= 65):
    print('requer aposentadoria: ')
elif (tempo_empr >= 30):
    print('requer aposentadoria: ')
elif (idade >= 60) and (tempo_empr >= 25):
    print('requer aposentadoria: ')
else:
    print('nao requer aposentadoria')    