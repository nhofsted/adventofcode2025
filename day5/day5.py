part1 = 0
ranges = []
with open("day5/Sample.txt", "r") as file:
    readingRanges = True
    for line in file:
        line = line.strip()
        if readingRanges:
            if len(line) == 0:
                readingRanges = False
                continue
            [begin, end] = line.split("-")
            ranges.append(range(int(begin), int(end) + 1))
        else:
            if next((True for r in ranges if int(line) in r), False):
                part1 += 1
print("part 1: ", part1)

part2 = 0
index = 0
ranges.sort(key=lambda r: r.start)
for r in ranges:
    if r.start >= index:
        part2 += len(r)
        index = r.stop
    elif index < r.stop:
        part2 += len(r) - index + r.start
        index = r.stop
print("part 2:", part2)
