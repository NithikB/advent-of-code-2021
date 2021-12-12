# Day 12 - Passage Pathing - Part 1
# https://adventofcode.com/2021/day/12


# import input file into graph
with open("day12_input.txt", 'r') as f:
    lines = f.read().splitlines()
    adjList = {}
    for line in lines:
        a, b = line.split("-")
        if a not in adjList:
            adjList[a] = [b]
        else:
            adjList[a].append(b)
        if b not in adjList:
            adjList[b] = [a]
        else:
            adjList[b].append(a)


# dfs function
def dfs(node):
    global count
    if node == "end":  # if end, add distinct path to count
        count += 1
        return
    elif node in visited:
        return

    # mark only lowercase nodes as visited to not visit again
    if node.lower() == node:
        visited.add(node)

    for n in adjList[node]:  # dfs on all neighbors
        dfs(n)

    # remove visited nodes from the set to allow for other paths
    if node.lower() == node:
        visited.remove(node)


count = 0
visited = set()
dfs("start")

print("Distinct Paths:", count)

# Day 12 - Passage Pathing - Part 2


# dfs function
def dfs(node):
    global count
    global second
    if node == "start" and visited:  # edge case to not visit start again
        return
    # if node in visited and we alr visited a lowercase node twice, stop
    elif node in visited and second:
        return
    elif node == "end":  # if end, add distinct path to count
        count += 1
        return

    # if node is alr visited, set second as the node we will visit twice
    if node in visited:
        second = node
    # mark only lowercase nodes as visited to not visit again
    elif node.lower() == node:
        visited.add(node)

    for n in adjList[node]:  # dfs on all neighbors
        dfs(n)

    if node == second:  # if we visited curr node twice, clear "second" var
        second = None
    elif node.lower() == node:  # remove visited node to allow for other paths
        visited.remove(node)


count = 0
visited = set()
# keep "second" variable to store the lowercase node that we visit twice
second = None
dfs("start")

print("Distinct Paths:", count)
