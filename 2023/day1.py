import re

def part1(input_file):
    with open(input_file, "r") as f:
        sum = 0
        for t in f.readlines():
            digs = re.findall('[0-9]', t)
            linenum = int(digs[0]+digs[-1])
            sum += linenum
        print(sum)

def get_num(input, the_numbers):
    try:
        value = int(input)
        return str(value)
    except ValueError:
        return str(the_numbers.index(input)+1)

def part2(input_file):
    with open(input_file, "r") as f:
        the_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        re_string = "(?=([0-9]|"+"|".join(the_numbers)+ "))"

        sum = 0
        for t in f.readlines():
            digs = re.findall(re_string, t)
            linenum = int(get_num(digs[0], the_numbers) + get_num(digs[-1], the_numbers)    )
            sum += linenum
        return sum

if __name__ == "__main__":
    ans = part2("input/day1.txt")
    print(ans)

    

