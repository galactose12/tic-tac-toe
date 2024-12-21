x_win = False
o_win = False
tie = False
nums = [1,2,3,4,5,6,7,8,9]
board = {
    1:1, 2:2, 3:3,
    4:4, 5:5, 6:6,
    7:7, 8:8, 9:9
}

#8 ways to win tic tac toe
#3 vertical: x["a1"] == 1 and x["a2"] == 1 and x["a3"] == 1 or x["b1"] == 1 and x["b2"] == 1 and x["b3"] == 1 or x["c1"] == 1 and x["c2"] == 1 and x["c3"] == 1
#3 horizontal: x["a1"] == 1 and x["b1"] == 1 and x["c1"] == 1 or x["a2"] == 1 and x["b2"] == 1 and x["c2"] == 1 or x["a3"] == 1 and x["b3"] == 1 and x["c3"] == 1
#2 diagonal: x["a1"] == 1 and x["b2"] == 1 and x["c3"] == 1 or x["a3"] == 1 and x["b2"] == 1 and x["c1"] == 1
winning_combinations = [
    [1,2,3],  # Row 1
    [4,5,6],  # Row 2
    [7,8,9],  # Row 3
    [1,4,7],  # Column 1
    [2,5,8],  # Column 2
    [3,6,9],  # Column 3
    [1,5,9],  # Diagonal 1
    [7,5,3]   # Diagonal 2
]

def check_win():
    for combination in winning_combinations:
        if all(board[cell] == 'O' for cell in combination):
            return 'O'
        if all(board[cell] == 'X' for cell in combination):
            return 'X'
    if all(board[cell] in xo for cell in list(board.keys())):
        return 'No one'
    return None
def print_board(a1 = '-', a2 = '-', a3= '-', b1= '-', b2= '-', b3= '-', c1= '-', c2= '-', c3= '-'):
    print("""             
     |     |     
  {0}  |  {3}  |  {6}  
_____|_____|_____
     |     |     
  {1}  |  {4}  |  {7}  
_____|_____|_____
     |     |     
  {2}  |  {5}  |  {8}  
     |     |     """.format(a1, a2, a3, b1, b2, b3, c1, c2, c3))

def play(p):
    print("{0} its you\'re turn!".format(p))
    space = input("Enter the space you want to play: ")
    try:
        space = int(space)
        if board[space] in nums:
            board[space] = p
        else:
            print("Space already taken!")
            play(p)
    except:
        print("Invalid input. Try again!")
        play(p)

print_board(*list(board.values()))
xo = ('O', 'X')
turn = 0
while True:
    #O plays
    play('O')
    print_board(*list(board.values()))
    if check_win():
        break
    #X plays
    play('X')
    print_board(*list(board.values()))
    if check_win() == 'X':
        break
    if check_win() == 'No one':
        break

print("{0} wins!".format(check_win()))