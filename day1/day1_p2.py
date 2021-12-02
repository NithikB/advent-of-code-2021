# Day 1: Sonar Sweep - Part 2

# import input file as depths in an array
with open("day1_input.txt", 'r') as f:
    depths = [int(line) for line in f]

count = 0
prevSum = depths[0] + depths[1] + depths[2]
for i in range(3, len(depths)):
    curr = prevSum + depths[i] - depths[i-3]
    if curr > prevSum:
        count += 1

print(count)