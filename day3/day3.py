# Day 3 - Binary Diagnostic - Part 1
# https://adventofcode.com/2021/day/3

from collections import defaultdict


# import input file into an array
with open("day3_input.txt", 'r') as f:
    nums = f.read().splitlines()

bits = len(nums[0])
n = len(nums)


def get_freq(nums):
    bits = len(nums[0])
    freq = defaultdict(int)
    for num in nums:
        for i in range(bits):
            freq[i] += int(num[i])
    return freq


freq = get_freq(nums)
gamma = ""
for bit in freq:
    if freq[bit] > n - freq[bit]:
        gamma += "1"
    else:
        gamma += "0"

gamma = int(gamma, 2)
epsilon = ~gamma & 0xfff

print("Power Consumption:", gamma * epsilon)


# Day 3 - Binary Diagnostic - Part 2

o2_nums = list(nums)
co2_nums = list(nums)

bit = 0
while len(o2_nums) > 1:
    freq, n = get_freq(o2_nums), len(o2_nums)
    reduced = []
    most = 1 if freq[bit] >= n - freq[bit] else 0
    for num in o2_nums:
        if int(num[bit]) == most:
            reduced.append(num)
    o2_nums = reduced
    bit += 1

bit = 0
while len(co2_nums) > 1:
    freq, n = get_freq(co2_nums), len(co2_nums)
    reduced = []
    least = 0 if freq[bit] >= n - freq[bit] else 1
    for num in co2_nums:
        if int(num[bit]) == least:
            reduced.append(num)
    co2_nums = reduced
    bit += 1

print("Life Support Rating:", int(co2_nums[0], 2) * int(o2_nums[0], 2))
