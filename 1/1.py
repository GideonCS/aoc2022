elf_totals = []
idx = 0
total=0
with open("./input.txt") as file:
    for line in file:
        stripped_line = line.rstrip()
        print(stripped_line)
        if not stripped_line:
            idx += 1
            elf_totals.append(total)
            total=0
            continue
        total+=int(stripped_line)
    # Need to include final set of totals
    elf_totals.append(total)

max = 0
for index, value in enumerate(elf_totals):
    if value > max:
        max = value

print(f'MAX_PART1={max}')
elf_totals.sort(reverse=True)
print(f'MAX PART2={sum(elf_totals[:3])}')