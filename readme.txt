Introduction:

This AI agent is coded to solve a 9x9 Sudokus as a NumPy input and returns a 9x9 NumPy array of solved Sudoku. The algorithm chosen is Constraint Satisfaction, where the agent will start at a position of an empty cell (filled with 0) and eliminate the possibilities (numbers ranging from 1-9) that are present in that cell’s column, row, and 3x3 sub-square. The agent is bounded by the rules of the games, which are the constraints.  

Functions:

A total of 6 functions listed below were used to solve the Sudoku puzzles:

get_possible_value(): This is the first function which will go through the Sudoku array and find an empty cell (filled with 0) and start eliminating the numbers present in the same row, column, and 3x3 sub-square from the list of possible values of this particular cell (each cell in the array is a list of possible numbers/values) and will return the array possible solutions after elimination. 

update_value(): This function will firstly find cells with singleton value by checking the size of each cell. The singleton value will then be removed from same row, column, and 3x3 sub-square and assign the singleton value to this particular cell because there is no other possibilities. The function finally returns two NumPy arrays one with actual assigned values and one with the possible values.

init(): This function acts more like an initialization function to create an empty 9x9 NumPy array of lists

is_goal(): This function will check all rows and columns and 3x3 squares to see if they contain integers from 1-9 and make it True if it is equal the values in possible_values, which means the goal is reached. It will be utilized in the sudoku_solver function to create an empty NumPy array. 

is_valid(): This function will check the input NumPy array for any duplicates in a column by saving them (if found) in a set, and afterwards checking for any set with length = 1 which indicates a duplicate was found. A 9x9 NumPy array of -1's will be returned if so, otherwise, the input array will continue to be processed by the other methods. One of the helpful methods from NumPy was used which is bicount that count the number of occurrences of each value in the array.

sudoku_solver(): The final function is where all the previous functions come together to solve the Sudoku puzzle. First, the input Sudoku will be checked for eligibility by is_valid(), if not, a 9x9 array of -1’s will be returned. Next, init() will be called to create an empty 9x9 NumPy array of lists, which will then be filled with values using get_possible_value() function by passing in the input Sudoku and the empty array.  N
ext, the function will check if the goal has not been reached by creating a while loop and limiting the attempts because it was noticed that at some difficulty levels, the agent will keep trying to solve the puzzles. To proceed, while the goal is not reached (using is_goal() function) the input Sudoku and array of possible values will be passed in update_value function to assign the singleton values to relative cells for a limited attempt of 100 times. Finally, once is_goal is True, the final values will be assigned to the input Sudoku by passing it to update_value. At the end of the function, a for loop were added after the agent got stuck with sudoku_easy number 1 problem from the test cell in Jupyter notebook. This for loop check is the solved Sudoku has any 0’s in the cells, which indicates the input puzzle is invalid and hence return a 9x9 array of -1’s.

References:

1- numpy.org. (n.d.). NumPy Documentation. [online] Available at: https://numpy.org/doc/.
2- Stack Overflow. (n.d.). python - NumPy array initialization (fill with identical values). [online] Available at: https://stackoverflow.com/questions/5891410/numpy-array-initialization-fill-with-identical-values [Accessed 16 Jan. 2021].
3- Stack Overflow. (n.d.). python - Determining duplicate values in an array. [online] Available at: https://stackoverflow.com/questions/11528078/determining-duplicate-values-in-an-array [Accessed 20 Jan. 2021].
4- Stack Overflow. (n.d.). Sudoku Checker in Python. [online] Available at: https://stackoverflow.com/questions/17605898/sudoku-checker-in-python [Accessed 20 Jan. 2021].
5- www.javatpoint.com. (n.d.). numpy.flatten() in Python - Javatpoint. [online] Available at: https://www.javatpoint.com/numpy-flatten [Accessed 20 Jan. 2021].
6- GeeksforGeeks. (2018). Python | set() method. [online] Available at: https://www.geeksforgeeks.org/python-set-method/ [Accessed 20 Jan. 2021].
7- Tech With Tim (2019). Python Sudoku Solver Tutorial with Backtracking p.2. YouTube. Available at: https://www.youtube.com/watch?v=lK4N8E6uNr4&t=773s&ab_channel=TechWithTim [Accessed 20 Jan. 2021].
8- Felicia (2019). Solving Sudoku with Python NumPy and set(). [online] Medium. Available at: https://medium.com/@feliciaSWE/solving-sudoku-with-python-numpy-and-set-95ca55f9ba01 [Accessed 5 Jan. 2021].






