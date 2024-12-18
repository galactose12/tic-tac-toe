x_win = False
o_win = False
tie = False

board = {
    "a1": '-', "a2": '-', "a3": '-',
    "b1": '-', "b2": '-', "b3": '-',
    "c1": '-', "c2": '-', "c3": '-'
}

#8 ways to win tic tac toe
#3 vertical: x["a1"] == 1 and x["a2"] == 1 and x["a3"] == 1 or x["b1"] == 1 and x["b2"] == 1 and x["b3"] == 1 or x["c1"] == 1 and x["c2"] == 1 and x["c3"] == 1
#3 horizontal: x["a1"] == 1 and x["b1"] == 1 and x["c1"] == 1 or x["a2"] == 1 and x["b2"] == 1 and x["c2"] == 1 or x["a3"] == 1 and x["b3"] == 1 and x["c3"] == 1
#2 diagonal: x["a1"] == 1 and x["b2"] == 1 and x["c3"] == 1 or x["a3"] == 1 and x["b2"] == 1 and x["c1"] == 1
winning_combinations = [
    ["a1", "a2", "a3"],  # Row 1
    ["b1", "b2", "b3"],  # Row 2
    ["c1", "c2", "c3"],  # Row 3
    ["a1", "b1", "c1"],  # Column 1
    ["a2", "b2", "c2"],  # Column 2
    ["a3", "b3", "c3"],  # Column 3
    ["a1", "b2", "c3"],  # Diagonal 1
    ["a3", "b2", "c1"]   # Diagonal 2
]

def check_win():
    for combination in winning_combinations:
        if all(board[cell] == 'O' for cell in combination):
            return 'O'
        if all(board[cell] == 'X' for cell in combination):
            return 'X'
    if all(board[cell] != '-' for cell in list(board.keys())):
        return 'No one'

def print_board(a1 = '-', a2 = '-', a3= '-', b1= '-', b2= '-', b3= '-', c1= '-', c2= '-', c3= '-'):
    print("""   a     b     c
      |     |     
1  {0}  |  {3}  |  {6}  
 _____|_____|_____
      |     |     
2  {1}  |  {4}  |  {7}  
 _____|_____|_____
      |     |     
3  {2}  |  {5}  |  {8}  
      |     |     """.format(a1, a2, a3, b1, b2, b3, c1, c2, c3))

def play(p):
    print("{0} its you\'re turn!".format(p))
    space = input("Enter the space you want to play: ")
    if board[space] == '-':
        board[space] = p
    else:
        print("Space already taken!")
        play(p)

print_board(*list(board.values()))

while True:
    #O plays
    play('O')
    print_board(*list(board.values()))
    if check_win() == 'O':
        break
    #X plays
    play('X')
    print_board(*list(board.values()))
    if check_win() == 'X':
        break
    if check_win() == 'No one':
        break

print("{0} wins!".format(check_win()))