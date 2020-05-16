import random

board = [[ random.randint(1,9) for _ in range(9) ] for _ in range(9) ]

f = open('board.txt','w')
for line in board:
    for num in line:
        f.write("%d " %num)
    f.write("\n")
f.close()