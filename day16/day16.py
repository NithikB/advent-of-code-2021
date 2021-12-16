# Day 16 - Packet Decoder - Part 1
# https://adventofcode.com/2021/day/16


# import input file into array of line
with open("day16_input.txt", 'r') as f:
    trans = f.read().splitlines()[0]

binary = bin(int(trans, 16))[2:].zfill(len(trans)*4)


def parse(i):

    version, id = binary[i:i+3], binary[i+3:i+6]
    i += 6
    if id == "100":
        # tempSum = 0
        while binary[i] == "1":
            # tempSum += int(binary[x+1:x+5])
            i += 5
        # tempSum += int(binary[x+1:x+5])
        i += 5
        return (int(version, 2), i)
    else:
        tempSum = int(version, 2)
        length = 15 if binary[i] == "0" else 11
        i += 1
        portion = int(binary[i:i+length], 2)
        i += length
        if length == 11:
            for _ in range(portion):
                val, i = parse(i)
                tempSum += val
        else:
            limit = i + portion
            while i < limit:
                val, i = parse(i)
                tempSum += val
        return (tempSum, i)

print("Version Sum:", parse(0)[0])


# Day 16 - Packet Decoder - Part 2

def parse(i):

    version, id = int(binary[i:i+3], 2), int(binary[i+3:i+6], 2)
    i += 6
    if id == 4:
        tempSum = ""
        while binary[i] == "1":
            tempSum += binary[i+1:i+5]
            i += 5
        tempSum += binary[i+1:i+5]
        i += 5
        return (int(tempSum, 2), i)
    
    tempSum = []
    length = 15 if binary[i] == "0" else 11
    i += 1
    portion = int(binary[i:i+length], 2)
    i += length
    if length == 11:
        for _ in range(portion):
            val, i = parse(i)
            tempSum.append(val)
    else:
        limit = i + portion
        while i < limit:
            val, i = parse(i)
            tempSum.append(val)
    
    if id == 0:
        return (sum(tempSum), i)
    elif id == 1:
        ans = 1
        for x in tempSum:
            ans *= x
        return (ans, i)
    elif id == 2:
        return (min(tempSum), i)
    elif id == 3:
        return (max(tempSum), i)
    elif id == 5:
        return (1 if tempSum[0] > tempSum[1] else 0, i)
    elif id == 6:
        return (1 if tempSum[0] < tempSum[1] else 0, i)
    elif id == 7:
        return (1 if tempSum[0] == tempSum[1] else 0, i)


print("Evaluated:", parse(0)[0])