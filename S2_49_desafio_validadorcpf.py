"""
#  49. Desafio - Valide um CPF  #

#  Processo:
CPF = 168.995.350-09
---------------------------------------------------
1 * 10 = 10             *       1 * 11 = 11 <-
6 * 9  = 54             *       6 * 10 = 60
8 * 8  = 64             *       8 * 9  = 72
9 * 7  = 63             *       9 * 8  = 72
9 * 6  = 54             *       9 * 7  = 63
4 * 5  = 25             *       5 * 6  = 30
3 * 4  = 12             *       3 * 5  = 15
5 * 3  = 15             *       5 * 4  = 20
0 * 2  = 0              *       0 * 3  = 0
total  = 297            *   ->  0 * 2  = 0
                        *       Total  = 343
                        *
11 - (297 % 11) = 11    *       11 - (343 % 11) = 9
11 > 9 = 0              *       9 > 9 = 9
Digito 1 = 0            *       Digito 2 = 9
"""

cpf = input('Informe o CPF: ')
posicao1 = 0
contador1 = 10
total1 = 0
posicao2 = 0
contador2 = 11
total2 = 0
sequencia = ''

#  verificando se é sequencia, exemplos: 00000000000, 11111111111, 22222222222...
for d in cpf:
    if d == cpf[0]:
        sequencia += d * len(cpf)
    break

if len(cpf) == 11 and cpf.isnumeric():

    #  se o CPF for diferente da variavel sequencia, continua
    if cpf != sequencia:
        cpf_iterable = cpf[:-2]
            
        #  verificando o penultimo digito
        for d in range(len(cpf_iterable)):
            valor1 = int(cpf_iterable[posicao1]) * contador1
            posicao1 += 1
            contador1 -= 1
            total1 += valor1

        valor1 = 11 - (total1 % 11)
        
        if valor1 > 9:
            primeiro_digito = 0
        else:
            primeiro_digito = valor1

        cpf_iterable += str(primeiro_digito)

        #  verificando o último digito
        for d2 in range(len(cpf_iterable)):
            valor2 = int(cpf_iterable[posicao2]) * contador2
            posicao2 += 1
            contador2 -= 1
            total2 += valor2

        valor2 = 11 - (total2 % 11)

        if valor2 > 9:
            segundo_digito = 0
        else:
            segundo_digito = valor2

        cpf_iterable += str(segundo_digito)

        if cpf_iterable == cpf:
            cpf_format = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
            print(f'O CPF {cpf_format} informado É VÁLIDO!')
        else:
            cpf_format = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
            print(f'O CPF {cpf_format} informção NÃO É VÁLIDO')
    
    else:
        print('O CPF informado não pode ser sequência!')

else:
    print('CPF informado está incorreto!')

