# Day 7 - The Treachery of Whales - Part 1
# https://adventofcode.com/2021/day/7

from collections import defaultdict


# import input file into array of crabs
with open("day7_input.txt", 'r') as f:
    crabs = list(map(int, f.read().splitlines()[0].split(',')))

minFuel = 100000000
for c in crabs:
    minFuel = min(minFuel, sum([abs(c - i) for i in crabs]))

print("Fuel:", minFuel)

# Day 7 - The Treachery of Whales - Part 2
minFuel = 1000000000000000
for c in range(min(crabs), max(crabs)):
    minFuel = min(minFuel, sum([abs(c - i)*(abs(c-i)+1)/2 for i in crabs]))

print("Fuel:", int(minFuel))

