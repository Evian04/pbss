This project aims to solve a sudoku grid using a backtracking function (`src/module/grid.py/Grid.solve()`)
To solve the sudoku, you must enter the grid line per line in a `.txt` file.
Each line of this file represent a line of the sudoku, and must contain 9 characters, the corresponding digit or a space if the cell is empty (make sure that there is 9 character in each lines even if the last chars are spaces)
Then, save your file, run the `main.py` python script and enter the path of your file (with `/` as separator). You can also switch the `is_process_displayed` variable in the `main.py` file on `False` (it's on `True` by default) in order to hide the process, because that can be a bit annoying after a moment. Finally, the scrpit will print the time it took (in seconds) to solve the grid.
If `Cannot solve the sudoku` appears, it means that the program didn't find any solution, and that there is an error in the given grid, so verify what you written in the `model.txt` file.