def computador_escolhe_jogada(n,m):
    if n > m:
        if n % (m + 1) == 0:
            retira = n - (m+1)
            if retira > m:
                retira = m
                
        else:
            if m == 1:
                retira = 1
                print("O computador tirou uma peça.")
            else:
                t = n
                while t > 0:
                    if t % (m+1) == 0:
                        retira = n - t
                        t = 0
                    else:
                        t -= 1
                if retira == 1:
                    print("O computador tirou uma peça.")
                else:
                    print("O computador tirou",retira,"peças")

    else:
        if n == 1:
            retira = 1
            print("O computador tirou uma peça.")
        else:
            retira = n
            print("O computador tirou",n,"peças")
        
    return retira


def usuario_escolhe_jogada(n,m):
    if n > 0:
        tirar = int(input("Quantas peças você vai tirar? "))
        
        if tirar > m:
            print("Oops! Jogada inválida! Tente de novo.")
            retirado = usuario_escolhe_jogada(n,m)
        else:
            if tirar == 1:
                retirado = 1
                print("Você tirou uma peça.")
            else:
                retirado = tirar
                print("Voce tirou",retirado,"peças.")
        
    return retirado


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print("Você começa!")
        while n > 0:
            retirados = usuario_escolhe_jogada(n,m)
            n = n - retirados
            if n <= 0:
                print("Fim do jogo! Você ganhou!")
                ganhador = "usuario"
            else:
                print("Agora restam",n,"peças no tabuleiro.")
                retirados = computador_escolhe_jogada(n,m)
                n = n - retirados
                if n <= 0:
                    print("Fim do jogo! O computador ganhou!")
                    ganhador = "computador"
                else:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print("Agora restam",n,"peças no tabuleiro.")
    else:
        print("Computador começa!")
        while n > 0:
            retirados = computador_escolhe_jogada(n,m)
            n = n - retirados
            if n <= 0:
                print("Fim do jogo! O computador ganhou!")
                ganhador = "computador"
            else:
                print("Agora restam",n,"peças no tabuleiro.")
                retirados = usuario_escolhe_jogada(n,m)
                n = n - retirados
                if n <= 0:
                    print("Fim do jogo! Você ganhou!")
                    ganhador = "usuario"
                else:
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print("Agora restam",n,"peças no tabuleiro.")
    if n < 0:
        ganhador = 0
    return ganhador




print("Bem-vindo ao jogo do NIM! Escolha: ")
print("1 - para jogar uma partida isolada ")
opcao = int(input("2 - para jogar um campeonato "))

if opcao == 1:
    print("Voce escolheu uma partida isolada!")
    partida()
else:
    print("Voce escolheu um campeonato!")
    # campeonato()