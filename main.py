def display_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def insert_numbers(grid):
    empty_cells = get_empty_cells(grid)
    while empty_cells:
        for cell in empty_cells:
            i, j = cell
            while True:
                try:
                    num = int(input(f"Enter the number for row {i + 1}, column {j + 1}: "))
                    if num < 0 or num > 9:
                        raise ValueError
                    grid[i][j] = num
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 9.")
        empty_cells = get_empty_cells(grid)

    return grid


def get_empty_cells(grid):
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells


def check_numbers(grid):
    # Check rows
    for i in range(9):
        seen = set()
        for j in range(9):
            num = grid[i][j]
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)

    # Check columns
    for j in range(9):
        seen = set()
        for i in range(9):
            num = grid[i][j]
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)

    # Check subgrids
    for block in range(9):
        seen = set()
        for i in range(3):
            for j in range(3):
                num = grid[3 * (block // 3) + i][3 * (block % 3) + j]
                if num != 0:
                    if num in seen:
                        return False
                    seen.add(num)

    return True



def main():
    sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    
    display_grid(sudoku_grid)

    solved_grid = insert_numbers(sudoku_grid)
    
    display_grid(solved_grid)

    if icheck_numbers(solved_grid):
        print("The Sudoku solution is valid.")
    else:
        print("The Sudoku solution is invalid.")
    

if __name__ == "__main__":
    main()
