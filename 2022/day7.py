import pathlib

def get_sizes(path):
    with open(path, 'r') as f:
        files_in_dir = dict()
        parent_dict = dict()
        line = f.readline()
        current_directory = '/'
        while line != '':  # slutten av filen

            if line.split()[0] == '$': #command from user
                if line.split()[1] == "cd":
                    if line.split()[2] != "..":
                        prev_directory = current_directory
                        current_directory = line.split()[2]
                        if current_directory in files_in_dir:
                            print("what")
                        parent_dict[current_directory] = prev_directory

                        files_in_dir[current_directory]=list()

                    else: #going up a directory

                        parent_list = files_in_dir[parent_dict[current_directory]]
                        if current_directory == 'btb':
                            print(parent_list)
                        if parent_list.index(current_directory) in parent_list:
                            parent_list[parent_list.index(current_directory)] = sum(files_in_dir[current_directory])

                        current_directory = parent_dict[current_directory]

                    line = f.readline()
                elif line.split()[1] == "ls":
                    line = f.readline()
                    while line.split()[0] != "$":
                        if line.split()[0].isnumeric():
                            files_in_dir[current_directory].append(int(line.split()[0]))
                        else:
                            files_in_dir[current_directory].append(line.split()[1])
                        line = f.readline()
                        if line == '':
                            break

        parent_dict['/'] = None

        while parent_dict[current_directory]:
            parent_list = files_in_dir[parent_dict[current_directory]]
            parent_list[parent_list.index(current_directory)] = sum(files_in_dir[current_directory])
            current_directory = parent_dict[current_directory]

    return files_in_dir

if __name__ == "__main__":
    path = "input/day7.txt"
    #puzzle_input = pathlib.Path(path).read_text().strip()
    files_in_dir = get_sizes(path)

    # Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
    total_size = 0
    for key in files_in_dir:
        if sum(files_in_dir[key]) <= 100000:
            total_size += sum(files_in_dir[key])

    print(total_size)

