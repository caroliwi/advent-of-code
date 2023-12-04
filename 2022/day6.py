import pathlib


def get_marker(puzzle_input, length) -> int:
    for i in range(length, len(puzzle_input)):
        if len(set((puzzle_input[i - length:i]))) == length:
            return i


if __name__ == "__main__":
    path = "input/day6.txt"
    puzzle_input = pathlib.Path(path).read_text().rstrip()
    answer = get_marker(puzzle_input, 14)
    print(answer)

def test_get_marker():
    assert(get_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7)