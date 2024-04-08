from Point_Line_Game.Board import Board
from Point_Line_Game.Checker import Checker
class Display:
    def __init__(self) -> None:
        self.alphabet = 'abcdefghij'
        # self.board_s = board_s
        # self.my_board = Board()
        # self.board_s = self.my_board.board_size()
        # self.my_board.create_board()

        # self.my_board2=Checker()
        # self.my_board2.check_line()
        # self.row_lines_h = self.my_board2.row_lines_h
        # # print(self.row_lines_h)
        # self.row_lines_p = self.my_board2.row_lines_p




    # get board object with its list and print the board on terminal (Moein)
    # gets ('a1', 'b1') as player input to update the board
    def display_board(self,board_s,row_lines):
        row_lines_h = row_lines[0]
        row_lines_p = row_lines[1]
        # print(row_lines_p)
        # Display alpahbet as title row
        column_marks = []
        for i in range (0,board_s):
          column_marks.append(self.alphabet[i])
          column = '     '.join(column_marks)
        print('    ' + column)

        # Display grid
        for row_counter in range(0,board_s):
          # Horizontal
          ## initialize
          row_horizontal = []

          #   row_lines_h = ['.','     ','.','     ','.','     ','.','     ','.','     ','.','     ','.','     ','.','     ','.','     ','.']

          ## Use output of other funcitons.
        #   row_lines_h [row_counter][2*0+1] = '_____'
          # row_lines_h [2][2*2+1] = '_____'
        #   row_lines_h [row_counter][2*4+1] = '_____'

          # perpendicular
          ## initialize
          row_perpendicular = []
          # row_lines_p =  [[''] * 20 for i in range(10)]
          # for i in range(10):
          #     for j in range(10):
          #         row_lines_p[i][2*j]=' '
          #         row_lines_p[i][2*j+1]='     '
          # row_lines_p = [' ','     ',' ','     ',' ','     ',' ','     ',' ','     ',' ','     ',' ','     ',' ','     ',' ','     ','']
          ## Use output of other funcitons.
        #   row_lines_p[row_counter][2*0] = '|'
        #   row_lines_p[row_counter][2*1] = '|'
          # row_lines_p[3][2*1] = '|'
        #   row_lines_p[row_counter][2*6+1] = '   M   '

          for column_counter in range(0,board_s*2-1):
              # H
              row_horizontal.append(row_lines_h [row_counter][column_counter])

              # P
              row_perpendicular.append(row_lines_p [row_counter][column_counter])

          horizontal = ''.join(row_horizontal)
          perpendicular = ''.join(row_perpendicular)

          if row_counter == 9:
            print(str(row_counter+1) + '  ' + horizontal)
          elif row_counter == board_s-1:
            print(str(row_counter+1) + '   ' + horizontal)
          else:
              print(str(row_counter+1) + '   ' + horizontal)
              print( '    ' + perpendicular)



    def display_turn(self, turn):
        pass

    def show_scores(self, players):
        pass

# game = Display()
# checker = Checker()
# a = list(checker.check_line())
# game.display_board(5,a)
