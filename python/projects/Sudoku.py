#                 Task: The department you work for
#has received a project that displays the solved sudoku puzzles
#in a digital environment. 

#Write a Python code to print out the given sudoku puzzle
#matrix in the following format.

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

# --------------------------------------------- #

count = 0
print("- - - - - - - - - - - - - - - ")
for i in sudoku:
    for j in range(9):
        print(i[j], " ", end="")
        if (j+1) == 9 : 
            print()
            count+=1
            if count%3==0 and count!=0 :
                print("- - - - - - - - - - - - - - - ")
        if (j+1) % 3 == 0 and j != 0 and j!=8: 
             print("| ", end="")
