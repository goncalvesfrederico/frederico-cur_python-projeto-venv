"""
##  JOGO DA FORCA  ##
"""

palavra_secreta = input('Informe a palavra secreta: ') 
print('Jogador 2 agora é sua vez de acertar!!!')

digitadas = []  #  lista vazia
chances = 3

while True:

    print()
    print(f'Letras já informadas: {digitadas}')

    if chances > 0:
        letra = input('Informe uma letra: ')  #  pegando a informação do jogador 2
        
        #  validando se o jogador 2 está apenas digitando 1 letra por vez!
        if len(letra) > 1:
            chances = chances - 1
            print(f'Opa isso não pode! Por favor digite apenas 1 letra. Agora você só tem {chances} chances')
            continue
        
        #armazenando as letras digitadas
        digitadas.append(letra)

        
        if letra in palavra_secreta:
            print(f'Isso ai você acertou a letra!!!')
            
            palavra_secreta_temp = ''  #  variavel da palavra secreta temporaria, para construção da palavra
            
            #  percorrendo a variavel palavra_secreta
            for letra_informada in palavra_secreta:
                if letra_informada in digitadas:
                    palavra_secreta_temp += letra_informada
                else:
                    palavra_secreta_temp += '*'

            print(palavra_secreta_temp)

            if palavra_secreta_temp == palavra_secreta:
                print(f'Parabéns você ACERTOU. A palavra era {palavra_secreta}')
                break
            else:
                continue
                
        
        else:
            chances = chances - 1
            print(f'A letra informada {letra} não existe na palavra secreta.')

        if chances > 1:
            print(f'Você possui {chances} chances')
        elif chances == 1:
            print(f'Você possui {chances} chance')
        else:
            print('Jogador 2, você perdeu! Acabou suas chances!!!')
            break

    else:
        print('Jogador 2, você perdeu! Acabou suas chances!!!')  
        break

