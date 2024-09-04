from random import seed, randrange

seed(None)

files: list[str] = ['dog.txt', 'science.txt', 'computer.txt']

all_lines: list[str] = []
for filename in files:
    with open(filename, "r") as file:
        all_lines.extend([ line.strip() for line in file ])

selected: int = randrange(0, len(all_lines))
print(all_lines[selected])
