class TickTackToe:
    # create empty board & set winner to None
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.winner = None
    
    # print board
    def print_board(self):
        print('+' + '---+'*3)
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print("| " + (" | ").join(row) + " |")
            print('+' + '---+'*3)
    
    # print board guide
    @staticmethod
    def print_board_nums():
        board_nums =  [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        
        print("Board Guide -")
        print('+' + '---+'*3)
        for row in board_nums:
            print("| " + (" | ").join(row) + " |")
            print('+' + '---+'*3)

    # return list of valid moves
    def get_valid_moves(self):
        return [i for i, value in enumerate(self.board) if value == ' ']
    
    # return count of valid moves
    def count_valid_moves(self):
        return len(self.get_valid_moves())
    
    # check if their exist an empty position on board
    def if_empty_position(self):
        return ' ' in self.board

    # check if someone wins or not
    def if_winner(self, position, symbol):
        # check row
        row_index = position // 3
        row = self.board[row_index*3 : (row_index + 1)*3]
        if all([value == symbol for value in row]):
            return True

        # check col
        col_index = position % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([value == symbol for value in column]):
            return True

        # check diagonals
        if position % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([value == symbol for value in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([value == symbol for value in diagonal2]):
                return True
        
        return False
            
    # place player's symbol on board
    def make_move(self, position, symbol):
        if self.board[position] == ' ':
            self.board[position] = symbol
            
            if self.if_winner(position, symbol):
                self.winner = symbol
            
            return True
        
        return False