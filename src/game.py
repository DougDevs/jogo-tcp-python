class Game():
    # Construtor que define as ações válidas do jogo
    def __init__(self):
        self.valid_actions = ['r', 'p', 't', 'd']
        
    # Método que resolve o jogo com base nas ações de cada jogador e retorna o resultado
    def resolve_game(self, p1_action, p2_action):
        if (p1_action == 'r' and p2_action == 't') or \
        (p1_action == 'p' and p2_action == 'r') or \
        (p1_action == 't' and p2_action == 'p'):
            return 1 # Jogador 1 ganha
        elif (p1_action == 't' and p2_action == 'r') or \
        (p1_action == 'r' and p2_action == 'p') or \
        (p1_action == 'p' and p2_action == 't'):
            return 2 # Jogador 1 perde
        else:
            return 3 # Empate

    # Método que retorna o nome completo da ação, dado um código de ação
    def get_action_fullname(self, action):
        if action == 'r':
            return 'Pedra(r)'
        elif action == 'p':
            return 'Papel(p)'
        else:
            return 'Tesoura(t)'

    # Método que verifica se uma ação é válida
    def is_valid(self, action):
        return action in self.valid_actions

    # Método que retorna todas as ações válidas, exceto a ação 'd' que representa desconexão
    def get_valid_actions(self):
        return self.valid_actions[:-1]

    # Método que verifica se uma ação é uma desconexão
    def check_disconnection(self, action):
        return True if action == 'd' else False