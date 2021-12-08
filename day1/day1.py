# Day 1: Sonar Sweep - Part 1
# https://adventofcode.com/2021/day/1

# import input file as depths in an array
with open("day1_input.txt", 'r') as f:
    depths = [int(line) for line in f]

count = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        count += 1

print("Answer: " + str(count))


# Day 1: Sonar Sweep - Part 2

count = 0
prevSum = depths[0] + depths[1] + depths[2]
for i in range(3, len(depths)):
    curr = prevSum + depths[i] - depths[i-3]
    if curr > prevSum:
        count += 1

print("Answer: " + str(count))
