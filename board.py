Board = {#block in board : corresponding move made
    '7': '', '8': '', '9': '',
    '4': '', '5': '', '6': '',
    '1': '', '2': '', '3': ''
}
#3x3
def printBoard():
    print(Board['7'] + ' |' + Board['8'] + ' |' + Board['9'])
    print('-+-+-')
    print(Board['4'] + ' |' + Board['5'] + ' |' + Board['6'])
    print('-+-+-')
    print(Board['1'] + ' |' + Board['2'] + ' |' + Board['3'])

printBoard()