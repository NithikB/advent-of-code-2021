# Day 2: Dive! - Part 1
# https://adventofcode.com/2021/day/2

# import input file into an array
with open("day2_input.txt", 'r') as f:
    commands = f.read().splitlines()

pos, depth = 0, 0
for command in commands:
    dir, val = command.split(" ")
    val = int(val)
    if dir == "up":
        depth -= val
    elif dir == "down":
        depth += val
    else:
        pos += val

print("Answer:", pos*depth)


# Day 2: Dive! - Part 2

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

print("Answer:", pos*depth)
