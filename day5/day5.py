# Day 4 - Hydrothermal Venture - Part 1
# https://adventofcode.com/2021/day/4

from collections import defaultdict


# import input file into array of nums and array of boards
def new_board(lines, i):
    board = []
    for x in range(i, i + 5):
        board.append(lines[x].strip().split())
    return board


with open("day4_input.txt", 'r') as f:
    lines = f.readlines()

    nums = lines[0].strip().split(",")

    boards = []
    for i in range(1, len(lines), 6):
        boards.append(new_board(lines, i+1))


def total(board):
    total = 0
    for row in board:
        for num in row:
            if num != "#":
                total += int(num)
    return total


def check(board):
    for row in board:
        count = 0
        for num in row:
            if num == "#":
                count += 1
        if count == 5:
            return total(board)

    for c in range(5):
        count = 0
        for r in range(5):
            if board[r][c] == "#":
                count += 1
        if count == 5:
            return total(board)

    return False


def mark(board, num):
    for r in range(5):
        for c in range(5):
            if board[r][c] == num:
                board[r][c] = "#"
                break


ans = -1
for num in nums:
    for board in boards:
        mark(board, num)

    for board in boards:
        if check(board):
            print(board)
            ans = check(board) * int(num)
            break
    if ans != -1:
        break


print("Score:", ans)

# Day 4 - Hydrothermal Venture- Part 2

with open("day4_input.txt", 'r') as f:
    lines = f.readlines()

    nums = lines[0].strip().split(",")

    boards = []
    for i in range(1, len(lines), 6):
        boards.append(new_board(lines, i+1))

i = 0
while len(boards) > 1:
    num = nums[i]

    for board in boards:
        mark(board, num)

    nextBoards = []
    for board in boards:
        if not check(board):
            nextBoards.append(board)
    boards = nextBoards
    i += 1

board = boards[0]
while not check(board):
    num = nums[i]
    mark(board, num)
    i += 1

print("Score:", check(board) * int(nums[i-1]))