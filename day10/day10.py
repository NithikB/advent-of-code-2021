# Day 10 - Syntax Scoring - Part 1
# https://adventofcode.com/2021/day/10


# import input file into array of lines
with open("day10_input.txt", 'r') as f:
    lines = f.read().splitlines()

points_key = {")": 3, "]": 57, "}": 1197, ">": 25137}
char_key = {"(": ")", "[": "]", "{": "}", "<": ">"}

score = 0
for line in lines:
    s = []
    for c in line:
        if c in char_key:
            s.append(c)
        elif s and c == char_key[s[-1]]:
            s.pop()
        else:
            score += points_key[c]
            break

print("Score:", score)

# Day 10 - Syntax Scoring - Part 2

points_key = {")": 1, "]": 2, "}": 3, ">": 4}
char_key = {"(": ")", "[": "]", "{": "}", "<": ">"}

scores = []
for line in lines:
    s = []
    valid = True
    for c in line:
        if c in char_key:
            s.append(c)
        elif s and c == char_key[s[-1]]:
            s.pop()
        else:
            valid = False
            break

    if not valid or not s:
        continue

    score = 0
    while s:
        c = s.pop()
        score *= 5
        score += points_key[char_key[c]]

    scores.append(score)

scores.sort()
print("Middle score:", scores[len(scores) // 2])
