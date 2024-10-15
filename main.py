game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def build_board():
    for row in game:
        print(" " + " | ".join(row) + " ")
        print("-----------")


def player_turn(turn):
    return "X" if turn % 2 == 0 else "O"


def player_choice(player):
    validchoice = False
    while not validchoice:
        choice = int(input("Select position 1-9 to select block: ")) - 1
        if choice < 0 or choice > 8:
            print("Out of range.")
        else:
            chosen_row = choice // 3
            chosen_column = choice % 3
            if game[chosen_row][chosen_column] == " ":
                game[chosen_row][chosen_column] = player
                validchoice = True
            else:
                print("Invalid choice. Position already occupied.")


def check_victory():
    # Check rows and columns
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != " ":
            return True
        if game[0][i] == game[1][i] == game[2][i] != " ":
            return True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] != " ":
        return True
    if game[0][2] == game[1][1] == game[2][0] != " ":
        return True
    return False


turns = 0

while turns < 9:
    build_board()
    current_player = player_turn(turns)
    player_choice(current_player)
    if check_victory():
        build_board()
        print(current_player + " wins!")
        break
    turns += 1

if turns == 9:
    build_board()
    print("It's a tie!")
