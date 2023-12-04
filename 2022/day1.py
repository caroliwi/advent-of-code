with open('input/day1.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    elf_sum_list = list()
    sum_elf = 0
    while line != '':  #slutten av filen
        if line != '\n':
            sum_elf += int(line)
        else:
            elf_sum_list.append(sum_elf)
            sum_elf = 0
        line = reader.readline()

elf_sum_list.append(sum_elf)

print(max(elf_sum_list))
print(f"top 3 sum: {sum(sorted(elf_sum_list, reverse = True)[:3])}")