#!/Users/jacobschreuder/.devops/bin/python3


def process_line_p1(line: str):
    max_joltage = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            joltage = int(line[i] + line[j])
            if joltage > max_joltage:
                max_joltage = joltage
    return max_joltage


def process_line_p2(line):
    to_skip = len(line) - 12
    skip_count = 0
    result = []

    i = 0
    while len(result) < 12 and i < len(line):
        remaining_after = len(line) - i - 1
        still_need = 12 - len(result)
        can_skip = remaining_after >= still_need

        if can_skip and skip_count < to_skip:
            best_ahead = max(line[i : i + (to_skip - skip_count) + 1])
            if line[i] < best_ahead:
                skip_count += 1
                i += 1
                continue

        result.append(line[i])
        i += 1

    return int("".join(result))


with open("day_3-input.txt") as f:
    instructions = f.read().strip().split("\n")

total_joltage = 0
for line in instructions:
    add = process_line_p1(line)
    total_joltage += add

print(total_joltage)

total_joltage = 0
for line in instructions:
    add = process_line_p2(line)
    total_joltage += add

print(total_joltage)
