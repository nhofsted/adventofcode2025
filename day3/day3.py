part1 = 0
part2 = 0

def maxBattery(line, start, remaining):
    max = 0
    maxIndex = 0
    for i in range(start, len(line) - remaining + 1):
        v = int(line[i])
        if(v > max):
            max = v
            maxIndex = i
    return max, maxIndex

def maxBank(line, batteries):
    bank = 0
    maxIndex = -1
    for i in range(0, batteries):
        max, maxIndex = maxBattery(line, maxIndex + 1, batteries - i)
        bank = bank * 10 + max
    return bank

with open("day3/sample.txt", "r") as file:
    for line in file:
        part1 += maxBank(line.rstrip(), 2)
        part2 += maxBank(line.rstrip(), 12)
print("part 1: ", part1)
print("part 2: ", part2)