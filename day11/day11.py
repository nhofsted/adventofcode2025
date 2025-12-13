import re

connections = {}
with open("day11/sample1.txt", "r") as file:
    for line in file:
        a, *b = re.split("[: ]+", line.strip())
        connections[a] = b


def reverse(connections):
    reversed = {}
    for a, bl in connections.items():
        for b in bl:
            if b in reversed:
                reversed[b].append(a)
            else:
                reversed[b] = [a]
    return reversed


def freeze(d):
    if isinstance(d, dict):
        return frozenset((key, freeze(value)) for key, value in d.items())
    elif isinstance(d, list):
        return tuple(freeze(value) for value in d)
    elif isinstance(d, tuple):
        return tuple(freeze(value) for value in d)
    return d


cache = {}


def calculateIncoming(reversed, sourceNode, targetNode):
    frozenkey = freeze(tuple([reversed, sourceNode, targetNode]))
    if frozenkey not in cache:
        if targetNode == sourceNode:
            cache[frozenkey] = 1
        elif targetNode not in reversed:
            cache[frozenkey] = 0
        else:
            cache[frozenkey] = sum(
                calculateIncoming(reversed, sourceNode, i) for i in reversed[targetNode]
            )
    return cache[frozenkey]


def calculateIncomingWithStops(connections, stops):
    product = 1
    for i in range(1, len(stops)):
        product *= calculateIncoming(reverse(connections), stops[i - 1], stops[i])
    return product


print("Part 1: ", calculateIncoming(reverse(connections), "you", "out"))

paths = [["svr", "fft", "dac", "out"], ["svr", "dac", "fft", "out"]]
print("Part 2: ", sum(calculateIncomingWithStops(connections, p) for p in paths))
