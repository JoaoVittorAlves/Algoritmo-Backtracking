# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque
from Pilha import resolver_labirinto_com_pilha


s = deque()


maze_csv_path = "labirinto1.txt"  # Substitua pelo caminho correto
maze = Maze() 

maze.load_from_csv(maze_csv_path)

# Exibir o lab
maze.run()
maze.init_player()

time.sleep(0.5)
tempo_espera = 0.5  
resolver_labirinto_com_pilha(maze, tempo_espera)





