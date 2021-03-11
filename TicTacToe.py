# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:56:57 2021

@author: felip
"""

class Board:
# _0_|_1_|_2_
# _3_|_4_|_5_
#  6 | 7 | 8 

    def __init__(self,game_name):
        self.current_turn = ''
        self.playerX_pos = []
        self.playerO_pos = []
        self.valid_positions = [0,1,2,3,4,5,6,7,8]
        self.win_conditions = ((0,1,2),
                               (3,4,5),
                               (6,7,8),
                               (0,3,6),
                               (1,4,7),
                               (2,5,8),
                               (0,4,8),
                               (2,4,6))             
        self.pos = ['_'] * 6
        for i in range(7,10,1):
            self.pos.append(' ')
        
    def __str__(self):    
       table = ('\n_'+str(self.pos[0])+'_|_'+str(self.pos[1])+'_|_'+str(self.pos[2])+'_')  
       table += ('\n_'+str(self.pos[3])+'_|_'+str(self.pos[4])+'_|_'+str(self.pos[5])+'_')  
       table += ('\n '+str(self.pos[6])+' | '+str(self.pos[7])+' | '+str(self.pos[8]))  
       return table
   
    def table_positions(self):
       print('_0_|_1_|_2_\n_3_|_4_|_5_\n 6 | 7 | 8  ')
               
    def reset_game(self,game_name):
        self.pos = ['_'] * 6
        for i in range(7,10,1):
            self.pos.append(' ')
            
    def check_win(self):
        for each_win in self.win_conditions:
            if all(positions in self.playerX_pos for positions in each_win):
                print('X venceu!')
                return True
            elif all(positions in self.playerO_pos for positions in each_win):
                print('O venceu!')   
                return True
        return 0    
            
    def change_pos(self,pos,player):        
        if (player=='X'):
            self.pos[pos] = 'X'
            self.playerX_pos.append(pos)
            self.check_win(self)
        elif (player=='O'):
            self.pos[pos] = 'O'
            self.playerO_pos.append(pos) 
            self.check_win(self)  
            
    def start_game(self):
        print('\nEssas são as posições do tabuleiro!')
        self.table_positions()
        self.current_turn = input('Quem começa? Digite X ou O: ')        
        while (not self.current_turn in ['X','O']):
            self.current_turn = input('Escolha apenas das opções disponíveis (X ou O): ')   
        self.reset_game(self)  
        if (self.game_flow()):
            print('Fim de jogo!')
        
    def game_flow(self):    
        while (len(self.playerO_pos)+len(self.playerX_pos)) < len(self.pos):
            print('É sua vez, '+str(self.current_turn)+'!')
            valid_entry=False     
            pos = int(input('Qual posição quer jogar? '))
            while (valid_entry==False):
                if (pos not in self.valid_positions):
                    pos = int(input('Escolha uma posição válida!'))
                elif ((pos in self.playerX_pos) or (pos in self.playerO_pos)):
                    pos = int(input('Esta posição já foi jogada antes!'))
                else:
                    valid_entry=True    
            self.pos[pos] = str(self.current_turn)
            if self.current_turn=='X':
                self.playerX_pos.append(pos)
                self.current_turn='O'
            else:
                self.playerO_pos.append(pos)
                self.current_turn='X'
            print(self)  
            if (self.check_win()):
                return 1
        
  
game = Board('PrimeiroGameEver')           
game.start_game()
