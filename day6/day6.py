import math
import re

problems = []
with open("day6/sample.txt", "r") as file:
    problems = [line.rstrip("\n") for line in file]

part1 = 0
numbers = [re.split(" +", problems[i].strip()) for i in range(0, len(problems) - 1)]
operators = re.split(" +", problems[-1].strip())
for i in range(0, len(operators)):
    column = [int(numbers[j][i]) for j in range(0, len(numbers))]
    match operators[i]:
        case "+":
            part1 += sum(column)
        case "*":
            part1 += math.prod(column)
print("part 1: ", part1)

part2 = 0
numbers = []
for c in range(len(problems[-1]) - 1, -1, -1):
    number = "".join([problems[j][c] for j in range(0, len(problems) - 1)]).strip()
    if len(number):
        numbers.append(int(number))
    if problems[-1][c] != " ":
        match problems[-1][c]:
            case "+":
                part2 += sum(numbers)
            case "*":
                part2 += math.prod(numbers)
        numbers = []
print("part 2: ", part2)
