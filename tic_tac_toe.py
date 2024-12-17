x_win = False
o_win = False
tie = False
x = {"a1":'-', "a2":'-', "a3":'-',"b1":'-', "b2":'-', "b3":'-', "c1":'-', "c2":'-', "c3":'-'}
o = {"a1":'-', "a2":'-', "a3":'-',"b1":'-', "b2":'-', "b3":'-', "c1":'-', "c2":'-', "c3":'-'}
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
            print("O wins!")
            break
        if all(board[cell] == 'X' for cell in combination):
            print("X wins!")

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



l = [1,1,1,1,1,1,1,1,1]
print(list(board.values()))
print(l == list(board.values()))

while x_win == False and o_win == False and tie == False:
    print("O it\'s your turn!")
    o_spot = input("Enter a space in grid (ex: a1)")
    if o_spot not in list(o.keys()):
        while o_spot not in list(o.keys()):
            print("Invalid input, try again.")
            o_spot = input("Enter a space in grid (ex: a1)")
    elif board[o_spot] == 1:
        print("Space already taken, try again.")
        while board[o_spot] == 1:
            print("Space already taken, try again.")
            o_spot = input("Enter a space in grid (ex: a1)")
    else:
        board[o_spot] == 1
        o[o_spot] == 1

