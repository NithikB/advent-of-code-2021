# Day 3 - Binary Diagnostic - Part 1
# https://adventofcode.com/2021/day/3

from collections import defaultdict


# import input file into an array
with open("day3_input.txt", 'r') as f:
    nums = f.read().splitlines()

bits = len(nums[0])
n = len(nums)

freq = defaultdict(int)
for num in nums:
    for i in range(bits):
        freq[i] += int(num[i])

gamma = ""
for bit in freq:
    if freq[bit] > n - freq[bit]:
        gamma += "1"
    else:
        gamma += "0"

gamma = int(gamma, 2)
epsilon = ~gamma & 0xfff

print("Answer:", gamma * epsilon)


# Day 3 - Binary Diagnostic - Part 2

o2 = 0
co2 = 0

o2_nums = list(nums)
co2_nums = list(nums)

# while len(o2_nums) > 0:
#     o2 += 1
#     o2_nums = [num for num in o2_nums if num[0] == "1"]

