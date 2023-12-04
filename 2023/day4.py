
def calculate_points(winning_numbers, my_numbers):
    matches = len(set(winning_numbers) & set(my_numbers))
    if matches > 0:
        points = 2 ** (matches - 1)
    else:
        points = 0
    return points
def part1(data):
    total = 0
    for line in data:
        winning_numbers = line.split(":")[1].split('|')[0].strip().split()
        #print(winning_numbers)
        my_numbers = line.split(":")[1].split('|')[1].strip().split()
        #print(my_numbers)
        points = calculate_points(winning_numbers, my_numbers)
        total+=points
    return total

def part2(data):
    match_vector = []
    for line in data:
        winning_numbers = line.split(":")[1].split('|')[0].strip().split()
        my_numbers = line.split(":")[1].split('|')[1].strip().split()
        match_vector.append(len(set(winning_numbers) & set(my_numbers)))
    #print(match_vector)
    count_vector = [1]*len(match_vector)
    for index, num in enumerate(match_vector):
        for idx in range(index + 1, index + num + 1):
            count_vector[idx] += count_vector[index]
    #print(count_vector)
    return sum(count_vector)
    #make a list of ones



if __name__ == "__main__":
    data = open("input/day4.txt").read().rstrip().split("\n")
    print(part2(data))
