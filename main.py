# Objective:
# 1. Create base structure of the game
# 2. Display the game grid
# 3. Insert the numbers in the grid
# 4. Check if the number is valid

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


def insert_numbers():
    ...


def check_numbers():
    ...


def main():
    display_grid()
    insert_numbers()
    check_numbers()


if __name__ == "__main__":
    main()