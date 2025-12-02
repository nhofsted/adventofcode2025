import re

pattern1 = re.compile("^(.+)\\1$")
pattern2 = re.compile("^(.+)(\\1)+$")
part1 = 0
part2 = 0
with open("day2/sample.txt", "r") as file:
    ranges =  file.readline().split(',')
    for _range in ranges:
        [begin, end]  = _range.split('-')
        for i in range(int(begin), int(end) + 1):
            if(pattern1.search(str(i))): part1 += i
            if(pattern2.search(str(i))): part2 += i
print("part 1: ", part1)
print("part 2: ", part2)