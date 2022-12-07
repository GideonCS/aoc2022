stacks = [
    ["V", "C", "W", "L", "R", "M", "F", "Q"],
    ["L", "Q", "D"],
    ["B", "N", "C", "W", "G", "R", "S", "P"],
    ["G", "Q", "B", "H", "D", "C", "L"],
    ["S", "Z", "F", "L", "G", "V"],
    ["P", "N", "G", "D"],
    ["W", "C", "F", "V", "P", "Z", "D"],
    ["S", "M", "D", "P", "C"],
    ["C", "P", "M", "V", "T", "W", "N", "Z"],
]

# Toggle Part_1 flag for part 1 solution, 1 crate at a time
def move_crates(
    crates: list, num_to_move: int, og_stack: int, new_stack: int, part_1: bool=False
):
    crates_copy = crates[:]
    movingCrates = crates[og_stack][:num_to_move]
    if part_1:
        movingCrates.reverse()
    crates_copy[og_stack] = crates_copy[og_stack][num_to_move:]
    crates_copy[new_stack] = movingCrates + crates_copy[new_stack]
    return crates_copy


with open("./input.txt") as file:
    for line in file:
        _, num_to_move, __, og_stack, ___, new_stack = line.strip().split()
        stacks = move_crates(
            stacks, int(num_to_move), int(og_stack) - 1, int(new_stack) - 1
        )

answer = ""
for row in stacks:
    answer += row[0]
print(answer)
