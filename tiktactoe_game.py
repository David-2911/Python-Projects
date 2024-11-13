# Variable Placeholders
game_on = True
board = ["#", "", "", "", "", "", "", "", "", ""]
player_names = ["", ""]
picks = ["", ""]


def clear_output():
    print("\n" * 2)


def welcome_message():
    global player_names  # Indicate that we're using the global variable
    print("#######################")
    print("Welcome to Tic Tac Toe!")
    print("#######################")
    print()

    # Get player names
    player_names[0] = input("Player 1, Enter your name: ")
    print()
    player_names[1] = input("Player 2, Enter your name: ")
    print()

    # Display the players
    print("#######################")
    print(f"{player_names[0]} vs {player_names[1]}!")
    print("#######################")
    print()

    # Get player 1's choice of X or O
    player1_pick = (
        input(f"{player_names[0]}, Do you want to play as X or O? ").strip().upper()
    )
    print()

    while player1_pick not in ["X", "O"]:
        print("Invalid input. Please enter either X or O.")
        player1_pick = (
            input(f"{player_names[0]}, Do you want to play as X or O? ").strip().upper()
        )
        print()

    # Assign player 2's pick based on player 1's choice
    picks[0] = player1_pick
    picks[1] = "O" if player1_pick == "X" else "X"

    # Display the picks
    print("#############################")
    print(f"{player_names[0]} is playing as {picks[0]}")
    print(f"{player_names[1]} is playing as {picks[1]}")
    print("#############################")
    print()


def display_board(board):
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("-------")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("-------")
    print(f"{board[1]} | {board[2]} | {board[3]}")


def position_choice(player):
    choice = "incorrect"
    while choice not in range(1, 10):
        choice = int(input(f"{player_names[player]}, choose a position: (1-9)  "))
        if choice not in range(1, 10) or board[choice] != "":
            print("Invalid Input! Position is either out of range or already taken.")
            choice = "incorrect"
    return choice


def replacement_choice(board, position, player):
    board[position] = picks[player]
    return board


def check_game():
    global game_on
    winning_combinations = [
        [board[1], board[2], board[3]],  # Row 1
        [board[4], board[5], board[6]],  # Row 2
        [board[7], board[8], board[9]],  # Row 3
        [board[1], board[4], board[7]],  # Column 1
        [board[2], board[5], board[8]],  # Column 2
        [board[3], board[6], board[9]],  # Column 3
        [board[1], board[5], board[9]],  # Diagonal 1
        [board[3], board[5], board[7]],  # Diagonal 2
    ]

    for combination in winning_combinations:
        if combination == ["X", "X", "X"]:
            print("X Won!")
            game_on = gameon_choice()
            return
        elif combination == ["O", "O", "O"]:
            print("O Won !")
            game_on = gameon_choice()
            return

    if "" not in board:
        print("Game Draw")
        game_on = gameon_choice()


def gameon_choice():
    choice = "incorrect"
    while choice not in ["Yes", "No"]:
        choice = input("Would you like to play again? (Yes or No)  ")
        if choice not in ["Yes", "No"]:
            clear_output()
            print("Invalid Input!")
    return choice == "Yes"


def reset_board():
    global board
    board = ["#", "", "", "", "", "", "", "", "", ""]


def main():
    # Welcome Message
    welcome_message()

    # Game Start
    global board
    clear_output()

    while game_on:
        reset_board()
        while game_on:
            display_board(board)
            clear_output()

            # Player 1
            position = position_choice(0)
            board = replacement_choice(board, position, 0)
            display_board(board)

            # Check if game is still ongoing
            check_game()

            if not game_on:
                break

            # Player 2
            position = position_choice(1)
            board = replacement_choice(board, position, 1)
            display_board(board)

            # Check if game is still ongoing
            check_game()


if __name__ == "__main__":
    main()
