import time
from maze import Maze
# estou tentando descobrir o porque de não estar respondendo depois que roda

class Pilha:
    def __init__(self):
        self.pilha = []
    
    def empurrar(self, item):
        #Adiciona um item à pilha.
        self.pilha.append(item)
    
    def tirar(self):
        #Remove e retorna o item do topo da pilha.
        return self.pilha.pop() if not self.esta_vazia() else None
    
    def esta_vazia(self):
        #Retorna True se a pilha estiver vazia.
        return len(self.pilha) == 0

def resolver_labirinto_com_pilha(maze: Maze, tempo_espera: float):
    pilha = Pilha()  # iniciando a pilha
    pilha.empurrar(maze.get_init_pos_player())  
    
    visitado = set()  # Conjunto de posições visitadas
    
    # Movimentos possíveis
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while not pilha.esta_vazia():  # Enquanto a pilha não estiver vazia
        linha, coluna = pilha.tirar()  # Tira o topo da pilha
        
        # avisa se encontrou o prêmio
        if maze.find_prize((linha, coluna)):
            print(f"Tesouro encontrado na posição ({linha}, {coluna})!")
            maze.mov_player((linha, coluna))
            maze.run()
            time.sleep(max(tempo_espera, 0.05))
            return True
        
        # Marca a posição como visitada
        visitado.add((linha, coluna))
        
        # Verifica as direções possíveis e adiciona à pilha
        for d_linha, d_coluna in direcoes:
            nova_linha, nova_coluna = linha + d_linha, coluna + d_coluna
            if maze.is_free((nova_linha, nova_coluna)) and (nova_linha, nova_coluna) not in visitado:
                pilha.empurrar((nova_linha, nova_coluna))  
                visitado.add((nova_linha, nova_coluna))  
        
        # Atualiza a posição do jogador e exibe o labirinto
        maze.mov_player((linha, coluna))
        maze.run()
    
    print("Caminho para o tesouro não encontrado.")
    return False

