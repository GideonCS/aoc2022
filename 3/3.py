
import string
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
total = 0

def get_priority(char):
    if char in lowercase:
        return lowercase.index(char)+1
    return uppercase.index(char)+27

with open("./input.txt") as file:
    for line in file:
        stripped_line = line.rstrip()
        length = len(stripped_line)
        sack1 = stripped_line[:length//2]
        sack2 = stripped_line[length//2:]
        for char in sack1:
            if char in sack2:
                total+=get_priority(char)
                break;
print(f'TOTAL PART 1={total}')

total=0
with open('./input.txt', 'r') as file:
    lines_gen = zip(*[file]*3)
    for lines in lines_gen:
        line1,line2,line3 =lines
        line1,line2,line3 = line1.strip(),line2.strip(),line3.strip()
        common_chars=list(set(line1)&set(line2)&set(line3))
        if common_chars:
            total+=get_priority(common_chars[0])

print(f'TOTAL PART 2={total}')
