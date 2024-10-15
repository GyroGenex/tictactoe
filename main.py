game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def build_board():
    row1 = " " + game[0][0] + " | " + game[0][1] + " | " + game[0][2] + " "

    row2 = " " + game[1][0] + " | " + game[1][1] + " | " + game[1][2] + " "

    row3 = " " + game[2][0] + " | " + game[2][1] + " | " + game[2][2] + " "
    blanks = "-----------"
    print(row1)
    print(blanks)
    print(row2)
    print(blanks)
    print(row3)


def player_turn(turn):
    piece = ""

    if turn % 2 == 0:
        piece = "X"
    else:
        piece = "O"

    return piece


def player_choice(player):

    validchoice = False

    while not validchoice:
        choice = int(input("Select position 1-9 to select block:"))-1
        if choice < 0 or choice > 8:
            print("out of range.")
        else:
            chosen_row = choice//3
            chosen_column = choice % 3
            if game[chosen_row][chosen_column] == " ":
                game[chosen_row][chosen_column] = player
                validchoice = True
            else:
                print("invalid choice. position already occupied")


def checkvictory():
    for row in range(len(game)):
        if game[row][0] == game[row][1] and game[row][0] == game[row][2] and game[row][0] != " ":
            print(1)
            return True
        for column in range(len(game[row])):
            if game[0][column] == game[1][column] and game[0][column] == game[2][column] and game[0][column] != " ":
                print(2)
                return True
    if game[0][0] == game[1][1] and game[0][0] == game[2][2] and game[0][0] != " ":
        print(3)
        return True
    elif game[0][2] == game[1][1] and game[0][2] == game[2][0] and game[0][2] != " ":
        print(4)
        return True
    else:
        return False


turns = 0

while turns < 9:
    player_choice(player_turn(turns))
    if checkvictory():
        build_board()
        print(player_turn(turns) + " wins!")
        break

    build_board()

    turns += 1
if turns == 9:
    print("It's a tie")
