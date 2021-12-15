# Day 15 - Chiton - Part 1
# https://adventofcode.com/2021/day/15

import heapq

# import input file into array of line
with open("day15_input.txt", 'r') as f:
    lines = f.read().splitlines()
    grid = [list(map(int, list(line))) for line in lines]

# modified djikstra's (djikstra finds shortest path)
# djikstra usually maintains a distance (default inf) for each node, a queue/heap for nodes, and a set of visited nodes
# djikstra start at the source and adds all unvisited neighbors to the queue, updating the distance to each neighbor 
# djikstras removes the min distance node from the queue and repeats the above steps until all nodes are visited

# we can modify and apply djikstras here until we visit the target, which happens when it is the min distance/risk node
# djikstra's guarantees us that the risk at that point is the smallest to reach the target

heap = [(0, 0, 0)]
v = set()
v.add((0, 0))
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
while heap:
    risk, r, c = heapq.heappop(heap)
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print("Risk:", risk)
        break

    for x, y in dir:
        r1, c1 = r + x, c + y
        if r1 < 0 or r1 >= len(grid) or c1 < 0 or c1 >= len(grid[0]):
            continue

        if (r1, c1) not in v:
            v.add((r1, c1))
            heapq.heappush(heap, (risk + grid[r1][c1], r1, c1))

# Day 15 - Chiton - Part 2
newGrid = []
for i in range(5):
    for row in grid:
        newRow = []
        for j in range(5):
            for x in row:
                newRow.append((x + i + j - 1) % 9 + 1)
        newGrid.append(newRow)
grid = newGrid

heap = [(0, 0, 0)]
v = set()
v.add((0, 0))
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
while heap:
    risk, r, c = heapq.heappop(heap)
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print("Risk:", risk)
        break

    for x, y in dir:
        r1, c1 = r + x, c + y
        if r1 < 0 or r1 >= len(grid) or c1 < 0 or c1 >= len(grid[0]):
            continue

        if (r1, c1) not in v:
            v.add((r1, c1))
            heapq.heappush(heap, (risk + grid[r1][c1], r1, c1))
