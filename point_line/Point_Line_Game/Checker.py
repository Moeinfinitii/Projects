import random
from Point_Line_Game.Player import Player
# from Player import __init__
class Checker:
    def __init__(self,players:list[Player]):
        # print('checker init')
        self.players = players
        self.last_winner = None

        self.num_squere = 0


        self.row_lines_h =  [[''] * 20 for i in range(10)]
        self.row_lines_h = [[''] * 20 for i in range(10)]
        for i in range(10):
            for j in range(10):
                self.row_lines_h[i][2*j]='.'
                self.row_lines_h[i][2*j+1]='     '
        
        self.row_lines_p =  [[''] * 20 for i in range(10)]
        self.row_lines_p =  [[''] * 20 for i in range(10)]
        for i in range(10):
            for j in range(10):
                self.row_lines_p[i][2*j]=' '
                self.row_lines_p[i][2*j+1]='     '
        

    def first_player(self):
        if self.last_winner != None:
            for player in self.players:
                if player.turn ==  self.last_winner:
                    player.turn = True
                    return player
        else:
            name_first_player = random.choice(self.players)
            name_first_player.turn = True
            return name_first_player
        
    def change_turn(self):
        for player in self.players:
          # player.turn =not (player.turn)
            if player.turn == True:
                player.turn = False
            else:
                player.turn = True

        for player in self.players:
            if player.turn == True:
              return player

    def win_check(self):
        if self.players[0].num_squere > self.players[1].num_squere:
            print(f'{self.players[0]} Won this game!')
            self.players[0].wingame += 1 
        
        elif self.players[1].num_squere > self.players[0].num_squere:
            print(f'{self.players[1]} Won this game!')
            self.players[0].wingame += 1 
        
        else:
            print('No one won.')


    def check_line(self,points):
        # print('checker line')
        # (a1,b1) to row_lines_h [row_counter][2*0+1] = '-----'
        line_tup = (points[0],points[1])
        # line_tup = ('b2','b3')
        # line_tup = ('c5','d5')
        # line_tup = ('c5','g5')

        line_alpha = ['','']
        line_num = ['','']
        for i in range (2):
            line_alpha[i] = line_tup[i][0]
            line_num[i] = int(line_tup[i][1])
        # print(line_num)
        # print(line_alpha)

        #alpha to num
        alpha2num = {'a': 1 , 'b' : 2 , 'c' : 3 , 'd' : 4 , 'e' : 5
                    ,'f' : 6 , 'g' : 7 , 'h' : 9 , 'i' : 10}
        keys_list = list(alpha2num.keys())


        for i in range(2):
            for j in range(len(alpha2num)):
                if line_alpha[i] == keys_list[j]:
                    line_alpha[i] = alpha2num[keys_list[j]]
        # print(line_alpha)

        
        # Horizontal line
        if line_num [0] == line_num[1] and abs(line_alpha[0]-line_alpha[1]) == 1:
            # print('H')
            num_column = min(line_alpha) - 1
            num_row = line_num [0] - 1
            if not self.row_lines_h [num_row][2*num_column+1] == '_____':
                self.row_lines_h [num_row][2*num_column+1] = '_____'
                is_line = True
            else:
                is_line = False
                print('The line is busy!!')
                return self.row_lines_h,self.row_lines_p,is_line


        # Prependicular line
        elif line_alpha[0] == line_alpha[1] and abs(line_num[0]-line_num[1]) == 1:
            # print('P')
            is_line = True
            num_row = min(line_num) - 1
            num_column = line_alpha[0]-1

            if not self.row_lines_p [num_row][2*num_column] == '|':
                self.row_lines_p [num_row][2*num_column] = '|'
            else:
                is_line = False
                print('The line is busy!!')
                return self.row_lines_h,self.row_lines_p,is_line

            # print(self.row_lines_p)
        else:
            print('Please select a correct line!')
            is_line = False
        return self.row_lines_h,self.row_lines_p,is_line

    def finish_check(self,total_squere,board_s):
        total = (board_s-1) ** 2
        if total_squere == total:
            return True
        else:
            return False
    
    def squere_check(self,player:Player,board_s,num_old_squere,sign):
        # from Display import Display
        # self.my_obj = Display()
        # self.board_s = self.my_obj.board_s()
        
        num_squere = 0
        for i in range(board_s-1):
            for j in range(board_s-1):
                if  self.row_lines_h[i][2*j+1] == '_____' and self.row_lines_h[i+1][2*j+1] == '_____' and self.row_lines_p[i][2*j] == '|' and self.row_lines_p[i][2*j+2] == '|' :
                    num_squere += 1
                    if self.row_lines_p[i][2*j+1] == '     ':
                        self.row_lines_p[i][2*j+1] = '  '+sign+'  '

        num_new_squere = num_squere - num_old_squere
        player.num_squere = player.num_squere + num_new_squere
        return num_squere,self.row_lines_p,player.num_squere
    
    def select_location(self,board_points):
       while True:  
            points =[]          
            f_s=['First','Secound']
            for i in range(2):
                while True:
                    point = input(f"{f_s[i]} point: ")
                    if point in board_points:
                        points.append(point)
                        break
                    else:
                        print('Select a correct point:')

            # print(points)            
            check_lines = self.check_line(points)
            if check_lines[2]:
                return check_lines[0],check_lines[1]
            

    def initialize(self):
        for player  in self.players:
            player.num_squere = 0

   
# check = Checker()
# Checker().check_line()