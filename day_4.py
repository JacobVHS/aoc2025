#!/Users/jacobschreuder/.devops/bin/python3


# Process a coordinate
def check_coord(grid: dict, row: int = 0, col: int = 0):
    if grid[(row, col)]:
        left = (row, col - 1) if col - 1 >= 0 else False
        right = (row, col + 1) if col + 1 >= 0 else False
        above = (row - 1, col) if row - 1 >= 0 else False
        above_right = (row - 1, col + 1) if row - 1 >= 0 and col + 1 >= 0 else False
        above_left = (row - 1, col - 1) if row - 1 >= 0 and col - 1 >= 0 else False
        below = (row + 1, col) if row + 1 >= 0 else False
        below_right = (row + 1, col + 1) if row + 1 >= 0 and col + 1 >= 0 else False
        below_left = (row + 1, col - 1) if row + 1 >= 0 and col - 1 >= 0 else False
        positions = [
            left,
            right,
            above,
            above_right,
            above_left,
            below,
            below_right,
            below_left,
        ]
        total = sum(grid[pos] for pos in positions if pos and pos in grid)
        return total < 4
    else:
        return False


if __name__ == "__main__":
    # Read puzzle input
    with open("day_4-input.txt", "r") as f:
        grid = {
            (row, col): char == "@"
            for row, line in enumerate(f)
            for col, char in enumerate(line.strip())
        }

    total = sum(check_coord(grid, row, col) for row, col in grid)
    print(total)
