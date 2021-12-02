# Day 2: Dive! - Part 1

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


print(pos*depth)
