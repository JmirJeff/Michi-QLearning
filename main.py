# Autor: JmirJeff

import numpy as np
import random

# definimos el entorno
class michi():
    def __init__(self):
        self.states = np.zeros((3,3))
        self.player1_turn = random.choice((True,False))
        self.player2_turn = not(self.player1_turn)
    def action(self, act):
        if self.player1_turn:
            v = 1
        else:
            v = 2
        if self.states.item(act)==0.0:
            self.states.itemset(act,v)
        else:
            print ('escoja una casilla vacia')
            return
        # turno del otro jugador
        self.player1_turn = self.player2_turn
        self.player2_turn = not(self.player1_turn)
    def verifica_ganador(self):
        for i in range(0,3):
            if self.states.item(i,0) == self.states.item(i,1) == self.states.item(i,2):
                if self.states.item(i,0) == 1:
                    return 'player1'
                else:
                    return 'player2'
            if self.states.item(0,i) == self.states.item(1,i) == self.states.item(2,i):
                if self.states.item(0,i) == 1:
                    return 'player1'
                else:
                    return 'player2'
        if self.states.item(0,0) == self.states.item(1,1) == self.states.item(2,2):
            if self.states.item(0,0) == 1:
                return 'player1'
            else:
                return 'player2'
        if self.states.item(0,2) == self.states.item(1,1) == self.states.item(2,0):
            if self.states.item(0,0) == 1:
                return 'player1'
            else:
                return 'player2'
        if self.states.min() == 0:
            return None
        else:
            return 'empate'



# crear la tabla q para el juego
q_table = np.zeros((3**9,9))

# Parametros
max_episodes = 5000
learning_rate = 0.1
gamma = 0.8

epsilon = 1.0
