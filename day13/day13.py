# Day 13 - Transparent Origami - Part 1
# https://adventofcode.com/2021/day/13


# import input file into array of lines
with open("day13_input.txt", 'r') as f:
    lines = f.read().splitlines()
    dots = lines[:953]
    instructions = lines[954:]
    rows = []
    cols = []
    for dot in dots:
        c, r = dot.split(',')
        rows.append(int(r))
        cols.append(int(c))
    grid = [[0 for i in range(max(cols)+1)] for i in range(max(rows)+1)]
    for i in range(len(rows)):
        grid[rows[i]][cols[i]] = 1

n, m = len(grid), len(grid[0])
dir, loc = instructions[0].split(" ")[2].split("=")
loc = int(loc)

for c in range(loc, m):
    for r in range(n):
        if grid[r][c] == 1:
            if loc - (c - loc) >= 0:
                grid[r][loc - (c - loc)] = 1
            grid[r][c] = 0
m = loc
count = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] == 1:
            count += 1
print("Count:", count)

# Day 13 - Transparent Origami - Part 2
with open("day13_input.txt", 'r') as f:
    lines = f.read().splitlines()
    dots = lines[:953]
    instructions = lines[954:]
    rows = []
    cols = []
    for dot in dots:
        c, r = dot.split(',')
        rows.append(int(r))
        cols.append(int(c))
    grid = [[0 for i in range(max(cols)+1)] for i in range(max(rows)+1)]
    for i in range(len(rows)):
        grid[rows[i]][cols[i]] = 1

n, m = len(grid), len(grid[0]) 
for i in instructions:
    dir, loc = i.split(" ")[2].split("=")
    loc = int(loc)
    if dir == "x":
        for c in range(loc, m):
            for r in range(n):
                if grid[r][c] == 1:
                    if loc - (c - loc) >= 0:
                        grid[r][loc - (c - loc)] = 1
                    grid[r][c] = 0
        m = loc
    else:
        for r in range(loc, n):
            for c in range(m):
                if grid[r][c] == 1:
                    if loc - (r - loc) >= 0:
                        grid[loc - (r - loc)][c] = 1
                    grid[r][c] = 0
        n = loc

for r in range(n):
    for c in range(m):
        if grid[r][c] == 1:
            print("█", end="")
        else:
            print(" ", end="")
    print()

with open("day13_out.txt", 'w') as f:
    grid = grid[:n][:c]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                grid[r][c] = "█"
            else:
                grid[r][c] = " "
    f.write("\n".join(str(row) for row in grid))
