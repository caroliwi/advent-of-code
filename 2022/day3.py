def get_priority(letter_in):
    # doing some magic
    if letter_in.islower():
        pri = ord(letter_in) - 96
    else:
        pri = ord(letter_in) - 38
    return pri


def part1(input_file):
    with open(input_file, "r") as f:
        total_pri = 0
        for bag in f.readlines():
            no_items = len(bag.strip())
            comp1 = bag[:int(no_items / 2)]
            comp2 = bag[int(no_items / 2):]
            common_list = [c for c in comp1 if c in comp2]
            total_pri += get_priority(common_list[0])
        print(total_pri)


def part2(input_file):
    with open(input_file, "r") as f:
        total_pri = 0
        bags = f.readlines()
        for i in range(0, len(bags), 3):
            common_list = [c for c in bags[i] if c in bags[i+1] and c in bags[i+2]]
            total_pri += get_priority(common_list[0])

        print(total_pri)

#part1("input/day3.txt")

part2("input/day3.txt")