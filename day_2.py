#!/Users/jacobschreuder/.devops/bin/python3


def check_for_duplicate_seq_p1(number):
    number_len = len(str(number))
    if number_len % 2 == 0:
        string_number = str(number)
        first_half = string_number[0 : number_len // 2]
        second_half = string_number[number_len // 2 : number_len]
        if first_half == second_half:
            return True
    return False


def check_for_duplicate_seq_p2(number):
    string_number = str(number)
    number_len = len(string_number)
    for seq_len in range(1, number_len // 2 + 1):
        if number_len % seq_len == 0:
            sequence = string_number[0:seq_len]
            repeats = number_len // seq_len
            if sequence * repeats == string_number:
                return True
    return False


with open("day_2-input.txt", "r") as f:
    data = f.read().strip().split(",")

ranges = [range(int(s), int(e) + 1) for item in data for s, e in [item.split("-")]]

# Part 1
invalid_sum = 0
for r in ranges:
    for num in r:
        if check_for_duplicate_seq_p1(num):
            invalid_sum += num
print(invalid_sum)

# Part 2
invalid_sum = 0
for r in ranges:
    for num in r:
        if check_for_duplicate_seq_p2(num):
            invalid_sum += num
print(invalid_sum)
