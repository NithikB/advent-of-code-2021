# Day 1: Sonar Sweep - Part 1

# import input file as depths in an array
with open("day1_input.txt", 'r') as f:
    depths = [int(line) for line in f]

count = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        count += 1

print(count)
