x_win = False
o_win = False
tie = False
x = {"a1":'-', "a2":'-', "a3":'-',"b1":'-', "b2":'-', "b3":'-', "c1":'-', "c2":'-', "c3":'-'}
o = {"a1":'-', "a2":'-', "a3":'-',"b1":'-', "b2":'-', "b3":'-', "c1":'-', "c2":'-', "c3":'-'}
board = {"a1":0, "a2":0, "a3":0,"b1":0, "b2":0, "b3":0, "c1":0, "c2":0, "c3":0}

#8 ways to win tic tac toe
#3 vertical: x["a1"] == 1 and x["a2"] == 1 and x["a3"] == 1 or x["b1"] == 1 and x["b2"] == 1 and x["b3"] == 1 or x["c1"] == 1 and x["c2"] == 1 and x["c3"] == 1
#3 horizontal: x["a1"] == 1 and x["b1"] == 1 and x["c1"] == 1 or x["a2"] == 1 and x["b2"] == 1 and x["c2"] == 1 or x["a3"] == 1 and x["b3"] == 1 and x["c3"] == 1
#2 diagonal: x["a1"] == 1 and x["b2"] == 1 and x["c3"] == 1 or x["a3"] == 1 and x["b2"] == 1 and x["c1"] == 1

def check_win():
    if x["a1"] == 'O' and x["a2"] == 'O' and x["a3"] == 'O' or x["b1"] == 'O' and x["b2"] == 'O' and x["b3"] == 'O' or x["c1"] == 'O' and x["c2"] == 'O' and x["c3"] == 'O' or x["a1"] == 'O' and x["b1"] == 'O' and x["c1"] == 'O' or x["a2"] == 'O' and x["b2"] == 'O' and x["c2"] == 'O' or x["a3"] == 'O' and x["b3"] == 'O' and x["c3"] == 'O' or x["a1"] == 'O' and x["b2"] == 'O' and x["c3"] == 'O' or x["a3"] == 'O' and x["b2"] == 'O' and x["c1"] == 'O':
        x_win == True
    if o["a1"] == 'O' and o["a2"] == 'O' and o["a3"] == 'O' or o["b1"] == 'O' and o["b2"] == 'O' and o["b3"] == 'O' or o["c1"] == 'O' and o["c2"] == 'O' and o["c3"] == 'O' or o["a1"] == 'O' and o["b1"] == 'O' and o["c1"] == 'O' or o["a2"] == 'O' and o["b2"] == 'O' and o["c2"] == 'O' or o["a3"] == 'O' and o["b3"] == 'O' and o["c3"] == 'O' or o["a1"] == 'O' and o["b2"] == 'O' and o["c3"] == 'O' or o["a3"] == 'O' and o["b2"] == 'O' and o["c1"] == 'O':
        o_win == True
    if board == list(board.values()) and x_win == False and o_win == False:
        tie == True
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

