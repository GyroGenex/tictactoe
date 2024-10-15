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
    validchoice = False

    while not validchoice:
        choice = int(input("Select position 1-9 to select block:"))-1
        if choice < 0 or choice > 8:
            print("out of range.")
        else:
            chosen_row = choice//3
            chosen_column = choice % 3
            if game[chosen_row][chosen_column] == " ":
                game[chosen_row][chosen_column] = piece
                validchoice = True
            else:
                print("invalid choice. position already occupied")

        build_board()


turns = 0

while turns < 9:
    player_turn(turns)

    turns += 1
