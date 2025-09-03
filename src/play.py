import os
from game import TickTackToe
from player import ComputerPlayer, HumanPlayer

# clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def play(game, player1, player2):
    # clear screen
    clear_screen()

    # print board guide
    game.print_board_nums()

    # set symbol to player1's symbol
    symbol = player1.symbol

    while game.if_empty_position():
        if symbol == player1.symbol:
            position = player1.get_move(game)
        else:
            position = player2.get_move(game)
        
        if game.make_move(position, symbol):
            print(f"\n{symbol} makes a move at {position}")
            game.print_board()
        
        if game.winner:
            print(f"\n{symbol} wins!")
            break

        symbol = player2.symbol if symbol == player1.symbol else player1.symbol

    if not game.winner:
        print("\nIt's a tie!")

# print main menu
def main_menu():
    print("\tTic-Tac-Toe\n")
    print("1 => Player v/s Player")
    print("2 => Player v/s Computer(AI)")
    print("3 => Exit\n")    

# game loop
while True:
    # clear screen
    clear_screen()

    # print main menu
    main_menu()
    
    # initialise players and game
    player1 = HumanPlayer('X')
    game = TickTackToe()

    # user input
    user_input = input("Select option (1-3) : ")

    # raise ValueError if 
    # user input is not a number (1-3)
    try:
        option = int(user_input)
        if option not in range(1, 4):
            raise ValueError
        valid_move = True
    except ValueError:
        continue

    if user_input == '1':
        player2 = HumanPlayer('O')
    elif user_input == '2':
        player2 = ComputerPlayer('O')
    else:
        print("\nBye!")
        break    

    # play game
    play(game, player1, player2)

    # return to main menu
    user_input = input("\nPress Enter to continue ...")
