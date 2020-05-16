# Sudoku using Backtracking
## ( main : run sudoku.py and press "S" )


# basic
->run sudoku-solver.py for the backtracking visualization using just python


# intermediate ( you will need pygame installed )
->run sudoku.py 

->enter a number after clicking a sqaure to see if you can play it there

### best part
->press "S" to watch it solve the puzzle using backtracking 


# to set a new board
->if you have pygame:
    run set-board.py to set the sudoku board
else:
    set the sudoku board manually inside the board.txt file



# requirements
->Python ( for the basic sudoku solver )

->Pygame to play sudoku ( main )

## extra info
to see the quickest way it can solve it using backtracking(ie. shifting the entire board to transport the grid with the highest amount of digits to the first position of the board and then solve),
click z_solve_board_quickest_visual.py ( pygame needed )

z_solve_board_quickest.py uses the above technique to solve the board quicker than the normal backtracking way, which is used in z_solve_board.py
