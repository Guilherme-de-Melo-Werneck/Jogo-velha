def imprimir_tabuleiro(tabuleiro):
    print("-------------")
    for i in range(3):
        for j in range(3):
            print("|", tabuleiro[i][j], "", end="")
        print("|")
        print("-------------")


def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True

    # Verificar colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False


def jogar_jogo_da_velha():
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    jogador1 = input("Digite o nome do jogador 1= ")
    jogador2 = input("Digite o nome do jogador 2= ")

    jogadores = [jogador1, jogador2]
    simbolos = ["X", "O"]

    jogador_atual = 0
    jogadas_restantes = 9

    while True:
        imprimir_tabuleiro(tabuleiro)

        print("É a vez de", jogadores[jogador_atual])

        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = simbolos[jogador_atual]
            jogadas_restantes -= 1

            if verificar_vitoria(tabuleiro, simbolos[jogador_atual]):
                print("Parabéns!", jogadores[jogador_atual], "venceu!")
                break

            if jogadas_restantes == 0:
                print("Empate!")
                break

            jogador_atual = (jogador_atual + 1) % 2
        else:
            print("Essa posição já está ocupada. Tente novamente.")


jogar_jogo_da_velha()