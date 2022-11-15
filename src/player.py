import random
import time
import math

# Player
class Player:
    # set symbol to ('X' or 'O')
    def __init__(self, symbol) -> None:
        self.symbol = symbol

    # get player's next move and 
    # return corresponding position on board
    def get_move(self):
        pass

# Computer Player inherit Player
class ComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        # pause
        time.sleep(1)

        # select ramdom position if board is empty
        if game.count_valid_moves() == 9:
            position = random.choice(game.get_valid_moves())
        else:
            # select position using minimax algorithm
            position = self.minimax(game, self.symbol)["position"]
        
        return position

    # recursive function
    def minimax(self, state, player):
        max_player = self.symbol
        other_player = 'O' if player == 'X' else 'X'

        # base case
        # checks if previous player wins
        if state.winner == other_player:
            return {
                "position" : None,
                "score" : 1 * (state.count_valid_moves() + 1) if other_player == max_player else -1 * (state.count_valid_moves() + 1)
            }
        # check if no valid moves left
        elif not state.if_empty_position():
            return {"position" : None, "score" : 0}
        
        if player == max_player:
            best_move = {"position" : None, "score" : -math.inf}
        else:
            best_move = {"position" : None, "score" : math.inf}
        
        # for all posible position
        for possible_position in state.get_valid_moves():
            # make move at possible position
            state.make_move(possible_position, player)
            
            # calculate simmulated sore
            sim_score = self.minimax(state, other_player)
            
            # undo move
            state.board[possible_position] = ' '
            state.winner = None
            sim_score["position"] = possible_position

            # update best move
            if player == max_player:
                if sim_score["score"] > best_move["score"]:
                    best_move = sim_score
            else:
                if sim_score["score"] < best_move["score"]:
                    best_move = sim_score
        
        return best_move

# Human Player inherit Player
class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        valid_move = False
        position = None

        # input move until its a valid move
        while not valid_move:
            user_input = input(f"\n{self.symbol}'s turn. Input move (0-8) : ")
            
            # raise ValueError if 
            # input move is not a number (0-8) or
            # not in vaild moves
            try:
                position = int(user_input)
                if position not in game.get_valid_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print("Invalid poistion. Try again!")
        
        return position