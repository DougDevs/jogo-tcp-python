import socket
# importa a classe Game do arquivo game.py
from game import Game
# define o endereço do host e a porta do servidor
HOST = "localhost"
PORT = 63337
# define o tamanho máximo dos dados recebidos pelo socket
SIZE = 1024
# define o formato de codificação dos dados enviados e recebidos pelo socket
FORMAT = "utf-8"
# cria uma instância do jogo
game = Game()
# função principal que controla o fluxo do jogo
def main():
    # cria um objeto socket e se conecta ao servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # exibe mensagens de introdução e confirmação de conexão
        log_msg = f"Conexão estabelecida com {HOST}:{PORT}"
        intro_msg = f"Este aplicativo é um jogo de Pedra, Papel, Tesoura (conhecido popularmente como Jokenpô).\
\n\nA cada iteração, você terá 4 opções, representadas por seus nomes seguidos de suas teclas de atalho entre parênteses. Você deve pressionar a tecla de atalho atribuída para ativar a função desejada.\
\n\nSe você escolher Pedra (r), papel (p) ou tesoura (t), jogará uma rodada do jogo e o servidor responderá com sua jogada, e o resultado da rodada será exibido na tela.\
\n\nSe você escolher desconectar (d), será desconectado do servidor e o jogo terminará.\
\n\nDivirta-se!!\
\n\n---------------------------------------------------------"
        print(log_msg, end='\n\n')
        print(intro_msg, end='\n\n')

        # loop principal do jogo
        while True:
            # solicita ao jogador a escolha de uma ação e valida a entrada
            client_action = input("Pedra (r), papel (p), tesoura (t) ou desconectar (d) > ").lower()
            while not game.is_valid(client_action):
                error_msg = f"Digite uma entrada válida."
                print(error_msg, end='\n\n')

                client_action = input("Pedra (r), papel (p), tesoura (t) ou desconectar (d) > ").lower()

            # envia a escolha do jogador para o servidor
            s.send(client_action.encode(FORMAT))

            # verifica se o jogador escolheu desconectar e encerra o jogo se for o caso
            if game.check_disconnection(client_action):
                outro_msg = f"Conexão encerrada com {HOST}:{PORT}. Obrigado por jogar!"
                print(outro_msg)
                break

            # se o jogador não escolheu desconectar, recebe a escolha do servidor e processa o resultado do jogo
            else:
                server_action = s.recv(SIZE).decode(FORMAT)
                print(f"[{HOST}:{PORT}] jogou {game.get_action_fullname(server_action)}")

                game_result = game.resolve_game(client_action, server_action)
                out_msg = f""

                if game_result == 1:
                    out_msg = f"Você ganhou. Parabéns!"
                elif game_result == 2:
                    out_msg = f"Você perdeu. Melhor sorte na próxima vez!"
                else:
                    out_msg = f"Empate!"

                print(out_msg, end='\n\n')

        s.close()

if __name__ == "__main__":
    main()
