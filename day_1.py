#!/Users/jacobschreuder/.devops/bin/python3


def solve(instructions):
    position = 50
    count = 0

    for line in instructions:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            position = (position - distance) % 100
        else:  # R
            position = (position + distance) % 100

        if position == 0:
            count += 1

    return count


def solve_part2(instructions):
    position = 50
    count = 0

    for line in instructions:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            # Count clicks that land on 0
            for i in range(1, distance + 1):
                position = (position - 1) % 100
                if position == 0:
                    count += 1
        else:  # R
            # Count clicks that land on 0
            for i in range(1, distance + 1):
                position = (position + 1) % 100
                if position == 0:
                    count += 1

    return count


with open("day_1-input.txt") as f:
    instructions = f.read().strip().split("\n")

print(solve(instructions))

print(solve_part2(instructions))
