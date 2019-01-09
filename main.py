# Autor: JmirJeff

import numpy as np
import random
from ast import literal_eval

# definimos el entorno
class michi():
    def __init__(self):
        self.reset()
    def reset(self):
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
    def actions_enabled(self):
        l = []
        for i in range(3):
            for j in range(3):
                if game.states[i,j] == 0.0:
                    l.append((i,j))
        return l


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
    def __init__(self,q_table,learning_rate,gamma,epsilon,max_epsilon,min_epsilon,delay_rate,game):
        self.table = q_table
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.max_epsilon = max_epsilon
        self.min_epsilon = min_epsilon
        self.delay_rate = delay_rate

        self.episode = 0

        self.game = game

    def play(self):
        if self.epsilon >random.random():
            # se ejecuta exploracion
            action = random.choices(game.actions_enabled())
        else:
            # se ejecuta explotacion
            action = np.argmax(self.table[int(self.game.q_table_state)])
        self.epsilon = self.min_epsilon + (self.max_epsilon - self.min_epsilon)*np.exp(-self.delay_rate*self.episode)
        self.episode += 1
        return (int(action/3),int(action%3))

    def upgrade_qtable(self,state,new_state,action,reward):
        self.q_table[state,action] += self.learning_rate*(reward + gama*np.max(self.q_table[new_state,:])-q_table[state,action])

print ('Iniciando...')
print ('Presione enter para iniciar...')
input()
print ('===================================')
print ('========== NUEVA PARTIDA ==========')
while (True):
    game = michi()
    #print (game.states)
    while (True):
        print (game.states)

        if (game.turn()==1):
            jugada = input('ingrese su jugada  - ')
            while (True):
                nex_turn = game.action(literal_eval(jugada))
                if (nex_turn):
                    break
        else:
            print ('El agente juega')

            game.action(random.choices(game.actions_enabled())[0])

        ganador = game.verifica_ganador()
        if ganador != None:
            if (ganador == 'player1'):
                print (game.states)
                print ('GANASTE')
            elif(ganador == 'player2'):
                print (game.states)
                print ('PERDISTE')
            elif (ganador == 'empate'):
                print (game.states)
                print ('EMPATE')
            print ('===================================')
            print ('========== NUEVA PARTIDA ==========')
            game.reset()
