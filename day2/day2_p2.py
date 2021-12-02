# Day 2: Dive! - Part 2
# https://adventofcode.com/2020/day/2

# import input file into an array
with open("day2_input.txt", 'r') as f:
    commands = f.read().splitlines()

pos, depth, aim = 0, 0, 0
for command in commands:
    dir, val = command.split(" ")
    val = int(val)
    if dir == "up":
        aim -= val
    elif dir == "down":
        aim += val
    else:
        pos += val
        depth += aim * val

print(pos*depth)
