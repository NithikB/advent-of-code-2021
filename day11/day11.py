# Day 11 - Dumbo Octopus - Part 1
# https://adventofcode.com/2021/day/11


# import input file into grid of octopi
with open("day11_input.txt", 'r') as f:
    grid = f.read().splitlines()
    for i in range(len(grid)):
        grid[i] = list(map(int, list(grid[i])))


def flash(r, c):
    if r < 0 or r >= 10 or c < 0 or c >= 10 or (r, c) in flashed:
        return 0

    grid[r][c] += 1
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1),
           (1, 1), (-1, -1), (1, -1), (-1, 1)]
    if grid[r][c] > 9:
        grid[r][c] = 0
        flashed.add((r, c))
        count = 1
        for x, y in dir:
            count += flash(r + x, c + y)
        return count

    return 0


flashes = 0
for i in range(100):
    flashed = set()
    for r in range(10):
        for c in range(10):
            grid[r][c] += 1
    for r in range(10):
        for c in range(10):
            if grid[r][c] > 9:
                flashes += flash(r, c)

print("Flashes:", flashes)

# Day 11 - Dumbo Octopus - Part 2
with open("day11_input.txt", 'r') as f:
    grid = f.read().splitlines()
    for i in range(len(grid)):
        grid[i] = list(map(int, list(grid[i])))
        
flashes = 0
i = 0
while True:
    i += 1
    flashed = set()
    for r in range(10):
        for c in range(10):
            grid[r][c] += 1
    for r in range(10):
        for c in range(10):
            if grid[r][c] > 9:
                flashes += flash(r, c)
    if len(flashed) == 100:
        break

print("Step All Flashed:", i)
