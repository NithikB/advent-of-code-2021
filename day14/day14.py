# Day 14 - Extended Polymerization - Part 1
# https://adventofcode.com/2021/day/14

from collections import Counter

# import input file into array of line
with open("day14_input.txt", 'r') as f:
    lines = f.read().splitlines()
    template = lines[0]
    pairs = lines[2:]
pairs = {k: v for k, v in (line.split(" -> ") for line in pairs)}

for i in range(10):
    newTemplate = ""
    for x in range(len(template)-1):
        pair = template[x:x+2]
        if pair in pairs:
            newTemplate += template[x] + pairs[pair]
        else:
            newTemplate += template[x]
    newTemplate += template[-1]
    template = newTemplate

count = Counter(template)
print("Max - Min:", max(count.values())-min(count.values()))


# Day 14 - Extended Polymerization - Part 2

with open("day14_input.txt", 'r') as f:
    lines = f.read().splitlines()
    template = lines[0]
    pairs = lines[2:]
pairs = {k: v for k, v in (line.split(" -> ") for line in pairs)}

pairFreq = {}
for i in range(len(template)-1):
    pair = template[i:i+2]
    pairFreq[pair] = pairFreq.get(pair, 0) + 1

count = Counter(template)
for i in range(40):
    newFreq = {}
    for pair in pairFreq:
        if pair in pairs:
            c = pairs[pair]
            count[c] = count.get(c, 0) + pairFreq[pair]
            pair1, pair2 = pair[0] + c, c + pair[1]
            newFreq[pair1] = newFreq.get(pair1, 0) + pairFreq[pair]
            newFreq[pair2] = newFreq.get(pair2, 0) + pairFreq[pair]
        else:
            newFreq[pair] = pairFreq.get(pair, 0)
    pairFreq = newFreq

print("Max - Min:", max(count.values())-min(count.values()))
