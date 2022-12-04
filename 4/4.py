def generate_list(low,high):
    return set(list(range(low,high+1)))

total=0
with open("./input.txt") as file:
    for line in file:
        elf_1, elf_2 = line.strip().split(',')
        elf_1,elf_2 = [int(x) for x in elf_1.split('-')], [int(x) for x in elf_2.split('-')]
        elf_1,elf_2 = generate_list(*elf_1), generate_list(*elf_2)
        if elf_1.issubset(elf_2) or elf_2.issubset(elf_1):
            total+=1

print(f'TOTAL={total}')

        
