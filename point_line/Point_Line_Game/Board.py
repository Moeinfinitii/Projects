class Board:
    def __init__(self):
        self.board_s = 0
        self.points = [ ]


    # create list of board and insert into Display class (Moein)
    def create_board(self):
        alphabet = 'abcdefghij'        
        board_points = []
        for i in range (1,self.board_s+1):
            for j in range (0,self.board_s):
                board_points.append(alphabet[j]+str(i))
        self.points = board_points
        # print(self.points)

    # 3-10 (Moein)
    def board_size(self):
        print('Please enter size of the game (between 3 and 10):')
        while True:
            size = input ('')
            try:
                self.board_s = int(size)
                if self.board_s > 10 or self.board_s < 3:
                    print("Your number isn't between 3 and 10:")
                else:
                    break
            except:
                print('Enter a number:')
        return self.board_s
    


    def clear(self):
        pass
board = Board()
board.create_board()