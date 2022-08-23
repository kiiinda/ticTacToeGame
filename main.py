
#block in board : corresponding move made

Board = {
    '7': '', '8': '', '9': '',
    '4': '', '5': '', '6': '',
    '1': '', '2': '', '3': ''
}
#3x3
def printBoard(board):
    print(board['7'] + ' |' + board['8'] + ' |' + board['9'])
    print('-+-+-')
    print(board['4'] + ' |' + board['5'] + ' |' + board['6'])
    print('-+-+-')
    print(board['1'] + ' |' + board['2'] + ' |' + board['3'])


#take input from user and verify
def game():
    turn = 'X'
    count = 0

    for (i) in range(10):
        printBoard(Board)
        print("Make your move" + turn)

        move = input()

        if Board[move] == ' ':
            Board[move] = turn
            count += 1

        else:
            print("That position is already filled.\nMove to another position")
            continue

#Check if either player has won after 5 moves
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ': # horizontal_top
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ': # horizontal_middle
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ': # horizontal_bottom
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            elif Board['7'] == Board['4'] == Board['1'] != ' ': # vertical_left-side
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['8'] == Board['5'] == Board['2'] != ' ': # vertical_middle
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['9'] == Board['6'] == Board['3'] != ' ': # vertical right-side
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

            elif Board['3'] == Board['5'] == Board['7'] != ' ': # diagonal
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ': # diagonal
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
        

        # If neither wins and the board is full, declare as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X' 