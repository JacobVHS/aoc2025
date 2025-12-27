#!/Users/jacobschreuder/.devops/bin/python3


def check_coord(grid: dict, row: int, col: int):
    if (row, col) not in grid or not grid[(row, col)]:
        return False

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
    total = sum(grid.get(pos, False) for pos in positions if pos)
    return total < 4


if __name__ == "__main__":
    with open("day_4-input.txt", "r") as f:
        grid = {
            (row, col): char == "@"
            for row, line in enumerate(f)
            for col, char in enumerate(line.strip())
        }

    total = sum(check_coord(grid, row, col) for row, col in grid)
    print(f"Part 1 answer: {total}")

    total_removed = 0

    while True:
        removable = [coord for coord in grid if check_coord(grid, coord[0], coord[1])]

        if not removable:
            break

        for coord in removable:
            grid[coord] = False

        total_removed += len(removable)

    print(f"Part 2 answer: {total_removed}")
