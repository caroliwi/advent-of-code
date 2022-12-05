import pathlib
import collections
import re
from itertools import chain

def part1(supplyStacks, moves):
    supplyStacks = move_stacks(supplyStacks, moves)
    answer = ''
    for i in range(1, len(supplyStacks) + 1):
        answer += supplyStacks[i][-1]
    return answer

def part2(supplyStacks, moves):
    supplyStacks = move_stacks2(supplyStacks, moves)
    answer = ''
    for i in range(1, len(supplyStacks) + 1):
        answer += supplyStacks[i][-1]
    return answer

def parse_stacks(stacks):

    supplyStacks = collections.defaultdict(list)
    for line in stacks.split('\n'):
        for pos in range(1, len(line), 4):
            if line[pos].isalpha():
                stackNo = int((pos)/4+1)
                supplyStacks[stackNo].insert(0,line[pos])
    return supplyStacks

def move_stacks(supplyStacks, moves):
    for move in moves.split('\n'):
        numbers = re.findall('[0-9]+', move)
        for i in range(0, int(numbers[0])):
            supplyStacks[int(numbers[2])].append(supplyStacks[int(numbers[1])].pop())
    return supplyStacks

def move_stacks2(supplyStacks, moves):
    for move in moves.split('\n'):
        numbers = re.findall('[0-9]+', move)
        amount, from_s, to_s = int(numbers[0]), int(numbers[1]), int(numbers[2])
        supplyStacks[to_s].append(supplyStacks[from_s][-amount:])
        supplyStacks[to_s]=list(chain(*supplyStacks[to_s]))
        del supplyStacks[from_s][-amount:]
    return supplyStacks

if __name__ == "__main__":
    path = "input/day5.txt"
    puzzle_input = pathlib.Path(path).read_text().rstrip()
    stacks, moves = puzzle_input.split('\n\n')
    supplyStacks = parse_stacks(stacks)
    #answer = part1(supplyStacks, moves)
    answer = part2(supplyStacks, moves)
    print(answer)

