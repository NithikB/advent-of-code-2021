# Day 5 - Hydrothermal Venture - Part 1
# https://adventofcode.com/2021/day/5

from collections import defaultdict


# import input file into array of lines
lineSeg = []
with open("day5_input.txt", 'r') as f:
    lines = f.read().splitlines()

    for line in lines:
        coord1, coord2 = line.split(' -> ')
        x1, y1 = coord1.split(',')
        x2, y2 = coord2.split(',')
        lineSeg.append([int(x1), int(y1), int(x2), int(y2)])

grid = [[0 for x in range(1000)] for y in range(1000)]

for line in lineSeg:
    x1, y1, x2, y2 = line
    if x1 == x2:  # vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] += 1

    elif y1 == y2:  # horizontal line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] += 1


count = 0
for x in range(1000):
    for y in range(1000):
        if grid[x][y] > 1:
            count += 1

print("Overlap:", count)


# Day 5 - Hydrothermal Venture - Part 2

grid = [[0 for x in range(1000)] for y in range(1000)]

for line in lineSeg:
    x1, y1, x2, y2 = line
    if x1 == x2:  # vertical line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] += 1
    elif y1 == y2:  # horizontal line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] += 1
    else:  # diagonal line
        xstep = 1 if x1 < x2 else -1
        ystep = 1 if y1 < y2 else -1
        grid[y1][x1] += 1
        while x1 != x2 or y1 != y2:
            x1 += xstep
            y1 += ystep
            grid[y1][x1] += 1

count = 0
for x in range(1000):
    for y in range(1000):
        if grid[x][y] > 1:
            count += 1

print("Overlap:", count)
