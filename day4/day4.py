def isRoll(grid, x, y):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return grid[y][x] != "."


def markFree(grid, x, y):
    if grid[y][x] != "@":
        return False
    neighbours = -1
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if isRoll(grid, x + dx, y + dy):
                neighbours += 1
    if neighbours < 4:
        grid[y][x] = "x"


def remove(grid):
    removed = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "x":
                grid[y][x] = "."
                removed += 1
    return removed


with open("day4/sample.txt", "r") as file:
    grid = [[c for c in line.rstrip()] for line in file]
    removals = []
    removed = True
    while removed:
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                markFree(grid, x, y)
        removals.append(remove(grid))
        removed = removals[-1] != 0

print("part 1: ", removals[0])
print("part 2: ", sum(removals))
