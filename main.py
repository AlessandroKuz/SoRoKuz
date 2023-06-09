# Objective:
# 1. Create base structure of the game
# 2. Display the game grid
# 3. Insert the numbers in the grid
# 4. Check if the number is valid

def display_grid():
    ...


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


def check_numbers():
    ...


def main():
    display_grid()
    insert_numbers()
    check_numbers()


if __name__ == "__main__":
    main()
