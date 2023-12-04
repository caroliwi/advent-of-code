import pathlib

def fully_contains(list1, list2):
    if len(list1) <= len(list2):
        common_set = [i for i in list1 if i in list2]
        return len(common_set) == len(list1)
    else:
        common_set = [i for i in list2 if i in list1]
        return len(common_set) == len(list2)

def overlaps(list1, list2):
    return [i for i in list1 if i in list2]

def part1(puzzle_input):
    answer = 0
    for line in puzzle_input.split():
        elf1 = list(map(int,line.split(',')[0].split('-')))
        elf1 = [*range(elf1[0],elf1[1]+1)]
        elf2= list(map(int,line.split(',')[1].split('-')))
        elf2 = [*range(elf2[0],elf2[1]+1)]
        if fully_contains(elf1, elf2):
            answer += 1
    return answer

def part2(puzzle_input):
    answer = 0
    for line in puzzle_input.split():
        elf1 = list(map(int,line.split(',')[0].split('-')))
        elf1 = [*range(elf1[0],elf1[1]+1)]
        elf2 = list(map(int,line.split(',')[1].split('-')))
        elf2 = [*range(elf2[0],elf2[1]+1)]
        if overlaps(elf1, elf2):
            answer += 1
    return answer

if __name__ == "__main__":
    path = "input/day4.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    print(part2(puzzle_input))

