def get_marker():
    buff = []
    LENGTH_OF_MESSAGE = 14
    with open("./input.txt") as file:
        for line in file:
            for idx, char in enumerate(line):
                next_four = line[idx : idx + LENGTH_OF_MESSAGE]
                next_four_set = set(next_four)
                if len(next_four_set) == LENGTH_OF_MESSAGE:
                    print(idx + LENGTH_OF_MESSAGE)
                    return


get_marker()
