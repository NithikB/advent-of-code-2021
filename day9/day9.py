# Day 9 - Smoke Basin - Part 1
# https://adventofcode.com/2021/day/9


# import input file into 2d grid
with open("day9_input.txt", 'r') as f:
    grid = f.read().splitlines()
    for i in range(len(grid)):
        grid[i] = list(map(int, list(grid[i])))

n = len(grid)


def checkLow(r, c):
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for x, y in dir:
        r1, c1 = r + x, c + y
        if 0 <= r1 < n and 0 <= c1 < n and grid[r][c] >= grid[r1][c1]:
            return False

    return True


risk = 0
for r in range(n):
    for c in range(n):
        if checkLow(r, c):
            risk += 1 + grid[r][c]

print("Risk:", risk)

# Day 9 - Smoke Basin - Part 2
visited = set()


def basinCount(r, c, prev):
    if r < 0 or r >= n or c < 0 or c >= n:
        return 0
    if prev >= grid[r][c] or grid[r][c] == 9 or (r, c) in visited:
        return 0
    visited.add((r, c))
    count = 1
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for x, y in dir:
        count += basinCount(r+x, c+y, grid[r][c])

    return count


basins = []
for r in range(n):
    for c in range(n):
        if checkLow(r, c):
            count = basinCount(r, c, -1)
            if len(basins) < 3:
                basins.append(count)
            else:
                for i in range(3):
                    if count > basins[i]:
                        basins.insert(i, count)
                        basins.pop(3)
                        break

print("Top 3:", basins[0] * basins[1] * basins[2])
