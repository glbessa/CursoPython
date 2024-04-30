import random

def gerar_tabuleiro() -> list[list[str]]:
    """
    Gera um novo tabuleiro
    """
    tabuleiro = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    """
    Imprime o tabuleiro
    """
    pass

def atualizar_tabuleiro(tabuleiro, linha, coluna, valor):
    """
    
    """
    pass

def jogada_do_x(tabuleiro, linha, coluna):
    atualizar_tabuleiro(tabuleiro, linha, coluna, "x")

def jogado_do_o(tabuleiro, linha, coluna):
    atualizar_tabuleiro(tabuleiro, linha, coluna, "o")

def verificar_jogada(tabuleiro, linha, coluna):
    pass

def verificar_ganhador(tabuleiro):
    pass

def main():
    """
    Juntar todas as partes
    """

    # Gerar tabuleiro
    tabuleiro = gerar_tabuleiro()
    turno = random.choice(["x", "o"]) # Inicia o turno aleatoriamente
    
    # Repetir até o jogo acabar
    # estrutura de repetição
        # imprimir tabuleiro
        # pedir para o jogador a linha e a coluna
        # verificar se o jogador pode fazer esse lance
        # atualizar tabuleiro
        #tabuleiro[0][0] = "x"
        # verificar se o jogador ganhou
        # dar o turno para o outro jogador

main()