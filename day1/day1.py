with open("day1/sample.txt", "r") as file:
    pos = 50
    part1 = 0
    part2 = 0
    for line in file:
        dir = 1 if line[0] == 'R' else -1
        offset = int(line[1:])
        part2 += ((dir * pos % 100) + offset) // 100
        pos = (pos + dir * offset) % 100
        if pos == 0: part1 += 1
    print("part 1: ", part1)
    print("part 2: ", part2)