# Autor: JmirJeff

import numpy as np
import random
from ast import literal_eval

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
            #print ('escoja una casilla vacia')
            return False
        # turno del otro jugador
        self.player1_turn = self.player2_turn
        self.player2_turn = not(self.player1_turn)
        return True
    def verifica_ganador(self):
        for i in range(0,3):
            if self.states.item(i,0) == self.states.item(i,1) == self.states.item(i,2) != 0.0:
                if self.states.item(i,0) == 1:
                    return 'player1'
                else:
                    return 'player2'
            if self.states.item(0,i) == self.states.item(1,i) == self.states.item(2,i) != 0.0:
                if self.states.item(0,i) == 1:
                    return 'player1'
                else:
                    return 'player2'
        if self.states.item(0,0) == self.states.item(1,1) == self.states.item(2,2) != 0.0:
            if self.states.item(0,0) == 1:
                return 'player1'
            else:
                return 'player2'
        if self.states.item(0,2) == self.states.item(1,1) == self.states.item(2,0) != 0.0:
            if self.states.item(0,2) == 1:
                return 'player1'
            else:
                return 'player2'
        if self.states.min() == 0:
            return None
        else:
            return 'empate'
    def turn(self):
        if self.player1_turn:
            return 1
        else:
            return 2

    def q_table_state(self):
        s = self.states
        a = (3**8*s[0,0]+3**7*s[0,1]+3**6*s[0,2]+
            3**5*s[1,0]+3**4*s[1,1]+3**3*s[1,2]+
            3**2*s[2,0]+3*s[2,1]+s[2,2])
        return a


# crear la tabla q para el juego
q_table = np.zeros((3**9,9))

# Parametros
max_episodes = 5000
learning_rate = 0.1
gamma = 0.8

epsilon = 1.0
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.01

# crea la clase de aprendizaje q learning
class q_learning():
    def __init__(self,q_table,learning_rate,gamma,epsilon,max_epsilon,min_epsilon,delay_rate):
        self.table = q_table
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.max_epsilon = max_epsilon
        self.min_epsilon = min_epsilon
        self.delay_rate = delay_rate

    def play():
        if self.epsilon >random.random():
            self.epsilon = self.epsilon - self.delay_rate
            # se ejecuta exploracion
            num_actions = self.table.shape[1]

        else:
            # se ejecuta explotacion
            pass

print ('Iniciando...')
print ('Presione enter para iniciar...')
input()
while (True):
    game = michi()
    print (game.states)
    while (True):
        if (game.turn()==1):
            jugada = input('ingrese su jugada')
            while (True):
                nex_turn = game.action(literal_eval(jugada))
                if (nex_turn):
                    break
        else:
            print ('la red juega')
            while (True):
                nex_turn = game.action(random.choices([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)])[0])
                if (nex_turn):
                    break
        ganador = game.verifica_ganador()
        if ganador == None:
            pass
        if (ganador == 'player1'):
            print (game.states)
            print ('ganaste')
            break
        elif(ganador == 'player2'):
            print (game.states)
            print ('te ganaron XD')
            break
        elif (ganador == 'empate'):
            print (game.states)
            print ('quedo en empate')
            break
        print (game.states)
