tabuleiro = [' ' for _ in range(9)]

def mostrar_tabuleiro():
    print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")

def verificar_vitoria(tab, jogador):
    # Combinações de vitória: linhas, colunas e diagonais
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Colunas
        [0, 4, 8], [2, 4, 6]             # Diagonais
    ]
    for condicao in vitorias:
        if tab[condicao[0]] == tab[condicao[1]] == tab[condicao[2]] == jogador:
            return True
    return False

def verificar_empate():
    return ' ' not in tabuleiro

def jogar():
    jogador_name = input("Digite o nome do jogador X: ")
    jogador_name = input("Digite o nome do jogador O: ")
    jogador_atual = 'X'
    jogador_se = { 'X': jogador_name, 'O': jogador_name }
    while True:
        mostrar_tabuleiro()
        jogada = input(f"Vez do jogador {jogador_atual}. Escolha uma posição (1-9): ")
        
        if not jogada.isdigit() or int(jogada) not in range(1, 10):
            print("Jogada inválida! Digite um número entre 1 e 9.")
            continue
            
        posicao = int(jogada) - 1
        
        if tabuleiro[posicao] != ' ':
            print("Espaço já ocupado. Escolha outro.")
            continue
            
        tabuleiro[posicao] = jogador_atual
        
        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro()
            print(f"Parabéns! O jogador {jogador_se[jogador_atual]} venceu!")
            break
            
        if verificar_empate():
            mostrar_tabuleiro()
            print("Deu velha! O jogo terminou em empate.")
            break
            
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

jogar()

# jogar novamente

while True:
    resposta = input("Deseja jogar novamente? (s/n): ").lower().strip()
    if resposta == 's':
        tabuleiro = [' ' for _ in range(9)]
        jogar()
    elif resposta == 'n':
        print("Obrigado por jogar!")
        break
    else:
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")