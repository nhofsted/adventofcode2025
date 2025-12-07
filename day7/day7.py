def addBeam(d, beam, duplicity):
    if beam in d:
        d[beam] += duplicity
    else:
        d[beam] = duplicity


beams = {}
splits = 0
with open("day7/sample.txt", "r") as file:
    for line in file:
        nextBeams = {}
        for i in range(0, len(line)):
            c = line[i]
            if c == "S":
                addBeam(nextBeams, i, 1)
            elif i in beams:
                if c == "^":
                    addBeam(nextBeams, i - 1, beams[i])
                    addBeam(nextBeams, i + 1, beams[i])
                    splits += 1
                else:
                    addBeam(nextBeams, i, beams[i])
        beams = nextBeams
print("part 1: ", splits)
print("part 2: ", sum([value for _, value in beams.items()]))
