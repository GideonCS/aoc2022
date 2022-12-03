elf_totals = []
idx = 0
total=0
with open("./input.txt") as file:
    for line in file:
        stripped_line = line.rstrip()
        if not stripped_line:
            idx += 1
            elf_totals.append(total)
            total=0
            continue
        total+=int(stripped_line)


max = 0
for index, value in enumerate(elf_totals):
    if value > max:
        max = value

print(f'MAX={max}')
