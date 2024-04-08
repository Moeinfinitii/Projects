# In the name of Allah

# This code produced for Point-Line game
from Point_Line_Game.Player import Player 
from Point_Line_Game.Checker import Checker
from Point_Line_Game.Display import Display
from Point_Line_Game.Board import Board
from IPython.display import clear_output
class Launceher:
    def __init__(self):
        print('Welcome')
        self.sign = ['','']
        self.name = ['','']
        self.players = ['','']
        self.number_of_squere = [0,0]
        # self.score_game = [0,0]
        
        
        
        # Define Players
        for i in range(2):
            self.name[i] = input('Player' + str(i+1) + ', please enter your name: ')
            self.players[i] = Player(self.name[i])
            self.sign[i]=  self.name[i][0].capitalize()
        if self.sign[0] == self.sign[1]:
            print("Player 2's sign is 'P'")
            self.sign[1] = 'P'
        
        # self.checker = Checker(self.players)
        # self.row_lines = [self.checker.row_lines_h,self.checker.row_lines_p]
        # self.player1 = Player(self.name[0])
        # self.player2 = Player(self.name[1])

        self.finish = False

    def PL_game(self):
        

        display = Display()
        board = Board()
        game = True

        while game: 
            self.checker = Checker(self.players)
            self.row_lines = [self.checker.row_lines_h,self.checker.row_lines_p]
            self.board_s = board.board_size()
            board.create_board()
            num_squeres = 0

            turn_player = self.checker.first_player()
            self.finish = False
            while not self.finish:
                

                clear_output()
                display.display_board(self.board_s,self.row_lines)
                print(f'Completed Squeres: {self.sign[0]} {self.players[0].num_squere} | {self.players[1].num_squere} {self.sign[1]}')
                

                print(f"{turn_player}'s turn")
                rows = self.checker.select_location(board.points)
                self.row_lines = list(rows)
                # self.row_lines = list(self.checker.check_line(points))


                for i in range(2):
                    if str(turn_player) == self.name[i]:
                        sign = self.sign[i]
                squere = self.checker.squere_check(turn_player,self.board_s,num_squeres,sign)
                
                self.finish = self.checker.finish_check(squere[0],self.board_s)

                if squere[0]==num_squeres:
                    turn_player = self.checker.change_turn()
            

                num_squeres = squere[0]

            display.display_board(self.board_s,self.row_lines)
            self.checker.win_check()
            print(f'\n{self.name[0]} {self.players[0].wingame} | {self.players[1].wingame} {self.name[1]}')
            Player.play_again() 
            self.checker.initialize           
            # self.row_lines[1] = sq_ch[1]
            # checker.squere_check(self.player2,self.board_s)



# launcher = Launceher()
# launcher.PL_game()
