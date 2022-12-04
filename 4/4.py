def generate_list(low, high):
    return set(list(range(low, high + 1)))


def get_elf_values(elf):
    val_range = [int(x) for x in elf.split("-")]
    return generate_list(*val_range)

total_part_1 = 0
total_part_2 = 0
with open("./input.txt") as file:
    for line in file:
        elf_1, elf_2 = line.strip().split(",")
        elf_1, elf_2 = get_elf_values(elf_1), get_elf_values(elf_2)
        if elf_1.issubset(elf_2) or elf_2.issubset(elf_1):
            total_part_1 += 1
        if elf_1 & elf_2:
            total_part_2 += 1

print(f"PART 1 TOTAL={total_part_1}")

print(f"PART 2 TOTAL={total_part_2}")
