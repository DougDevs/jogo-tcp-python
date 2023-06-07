import threading
import socket
import random
from game import Game

HOST = "192.168.3.70"
PORT = 63337
TAMANHO_BUFFER = 1024
FORMATO = "utf-8"

game = Game()

def manipulador_de_conexao_cliente(conn, addr):
    """
    Função que será executada em uma thread para manipular a conexão com um cliente.
    Recebe como parâmetros um objeto de conexão e um endereço de IP e porta remotos.
    """
    while True:
        # Recebe a ação escolhida pelo cliente
        acao_cliente = conn.recv(TAMANHO_BUFFER).decode(FORMATO)

        # Verifica se o cliente encerrou a conexão ou se houve desconexão inesperada
        if not acao_cliente or game.check_disconnection(acao_cliente):
            print(f"Conexão encerrada por {addr}")
            break
        else:
            # Exibe a ação escolhida pelo cliente
            print(f"[{addr}] > {acao_cliente}")

            # Escolhe uma ação aleatória para o servidor
            acao_servidor = random.choice(game.get_valid_actions())

            # Exibe a ação escolhida pelo servidor
            print(f"[SERVIDOR] > {acao_servidor}")

            # Envia a ação escolhida pelo servidor de volta para o cliente
            conn.send(acao_servidor.encode(FORMATO))

    # Fecha a conexão com o cliente
    conn.close()

def main():
    # Cria um objeto de socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Associa o socket ao endereço de IP e porta desejados
        s.bind((HOST, PORT))
        # Aguarda conexões de clientes
        s.listen()

        print(f"Servidor está ouvindo em {HOST}:{PORT}")

        while True:
            # Aceita uma conexão e recupera o objeto de conexão e o endereço do cliente
            conn, addr = s.accept()
            print(f"Conexão estabelecida com {addr}")
            
            # Cria uma nova thread para manipular a conexão com o cliente
            thread = threading.Thread(target=manipulador_de_conexao_cliente, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    main()
