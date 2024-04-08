# from Board import Board
# from Checker import Checker
class Player:
    def __init__(self,name) -> None:
        self.marker = None
        self.name = name
        self.num_squere = 0
        self.turn = False

        self.wingame = 0

    def __str__(self):
      return self.name
    
    def play_again():
        print('Play again (Y/N)')
        while True:
            play = input()
            if play=='N' or play =='n':
                return False
            elif play=='y' or play =='Y':
                return True
            else:
                print('Please enter Y or N:')


    # def select_location(self,board_points,checker:Checker):
    #    while True:  
    #         points =[]          
    #         f_s=['First','Secound']
    #         for i in range(2):
    #             while True:
    #                 point = input(f"{f_s[i]} point: ")
    #                 if point in board_points:
    #                     points.append(point)
    #                     break
    #                 else:
    #                     print('Select a correct point:')

    #         # print(points)            
    #         check_line = checker.check_line(points)
    #         if check_line[2]:
    #             return check_line[0],check_line[1]

                
    
    # def cal_score(self,checker: Checker, board: Board):
       

    # def choose_position(self, board: Board):
    #     # cheker : check input
    #     while True:
    #         position=input('Dear '+ self.name +' please choose a position:')
    #         if position.isdigit():
    #             position=int(position)
    #             if position in range(1,10) and board.free_space(position): #board command
    #                 return position



    # def cal_score(self, checker, board: Board):
    #   checker_obj = Checker
    #   checker_obj.finish_check()
    #   win = checker.squere_check(board_list, self.name)
    #   if win:
    #     self.score += 1
    #   return win
    

# my_obj = Player('hasan')
# my_obj.player_names()



    # def __init__(self) -> None:
    #     # player_lines = [('a1', 'b1'), ...]
    #     self.turn = False
    #     pass

    # # selects the line and stores it in a list as [('a1', 'b1'), ...] (Hossein)
    # def player_input(self, checker):
    #     pass

    # def cal_point(self):
    #     pass

    # def player_turn(self):
    #     pass

    # def player_names():
    #     pass