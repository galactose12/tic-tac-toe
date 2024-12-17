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

print_board()
p1_name = input("Enter player 1 (O) name: ")
p2_name = input("Enter player 2 (X) name: ")

