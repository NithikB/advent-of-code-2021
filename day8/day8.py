# Day 8 - Seven Segment Search - Part 1
# https://adventofcode.com/2021/day/8


# import input file into array of lines
with open("day8_input.txt", 'r') as f:
    lines = f.read().splitlines()
    nums, displays = [], []
    for line in lines:
        x, y = line.split(" | ")
        x, y = x.split(" "), y.split(" ")
        nums.append(x)
        displays.append(y)


count = 0
valid = [2, 3, 4, 7]
for display in displays:
    for num in display:
        if len(num) in valid:
            count += 1

print("Count:", count)

# Day 8 - Seven Segment Search - Part 2


def getOrder(i):
    x, y = nums[i], displays[i]
    x.sort(key=lambda x: len(x))
    order = [""] * 7
    # find seg 0
    for c in x[1]:
        if c not in x[0]:
            order[0] = c
            break

    # find seg 2 and 5
    for seg in x[6:9]:
        if x[0][0] not in seg:
            order[2], order[5] = x[0][0], x[0][1]
            break
        if x[0][1] not in seg:
            order[5], order[2] = x[0][0], x[0][1]
            break

    # find seg 3 and 6
    left = 0
    for num in x[3:6]:
        if set(x[1]) < set(num):
            left = set(num)-set(x[1])
            break

    for num in x[6:9]:
        for c in left:
            if c not in num:
                order[3] = c
                break
        if order[3]:
            break

    for c in left:
        if c not in order:
            order[6] = c
            break

    # find seg 1
    for c in x[2]:
        if c not in order:
            order[1] = c
            break

    # find seg 4:
    for c in x[9]:
        if c not in order:
            order[4] = c
            break

    return order


patterns = {0: "012456", 1: "25", 2: "02346", 3: "02356", 4: "1235",
            5: "01356", 6: "013456", 7: "025", 8: "0123456", 9: "012356"}

ans = 0
for i in range(len(nums)):
    order = getOrder(i)
    digits = [0] * 10
    for k, v in patterns.items():
        seg = ""
        for d in v:
            seg += order[int(d)]
        digits[k] = set(seg)
    
    display = ""
    for each in displays[i]:
        for i in range(10):
            if digits[i] == set(each):
                display += str(i)
                break
    ans += int(display)

print("Total:", ans)