# Day 6 - Lanternfish - Part 1
# https://adventofcode.com/2021/day/6

from collections import defaultdict


# import input file into array of fish
with open("day6_input.txt", 'r') as f:
    fish = list(map(int, f.read().splitlines()[0].split(',')))

# brute force un-optimized
for i in range(80):
    newArr = []
    for f in fish:
        if f == 0:
            newArr.extend([6, 8])
        else:
            newArr.append(f-1)
    fish = newArr

print("Fish:", len(fish))

# Day 6 - Lanternfish - Part 2
with open("day6_input.txt", 'r') as f:
    fish = list(map(int, f.read().splitlines()[0].split(',')))

# optimized
counts = defaultdict(int)
for f in fish:
    counts[f] += 1
counts[0] = 0

for i in range(256):
    at0 = counts[0]
    for i in range(8):
        counts[i] = counts[i+1]
    counts[6] += at0
    counts[8] = at0

print("Fish:", sum([counts[i] for i in range(9)]))