import time
from functools import cache


def findLightsCombination(targetLights, buttons):
    todo = [[False for i in range(0, len(targetLights))]]
    if todo[0] == targetLights:
        return 0
    depth = 1
    while True:
        next = []
        for lights in todo:
            for button in buttons:
                nextLights = lights.copy()
                for i in range(0, len(button)):
                    nextLights[button[i]] = not nextLights[button[i]]
                if nextLights == targetLights:
                    return depth
                next.append(nextLights)
        todo = next
        depth += 1


def recurseJoltagesCombination(targetJoltages, buttons, visited, bestResult):
    index = findBestNextButton(len(targetJoltages), buttons, visited)

    button = buttons[index]
    maxButtonPresses = min(targetJoltages[toggle] for toggle in button)

    nextVisited = list(visited)
    nextVisited[index] = True

    required = targetJoltages.copy()
    for i in range(0, len(buttons)):
        if not nextVisited[i]:
            for toggle in buttons[i]:
                required[toggle] = 0
    minButtonPresses = max([required[toggle] for toggle in button])

    todo = targetJoltages.copy()
    for toggle in button:
        todo[toggle] -= maxButtonPresses
    maxButtonPresses = min(maxButtonPresses, bestResult - max(todo))

    for i in range(minButtonPresses, maxButtonPresses + 1):
        nextTargetJoltages = targetJoltages.copy()
        for toggle in button:
            nextTargetJoltages[toggle] -= i

        if False in nextVisited:
            result = recurseJoltagesCombination(
                nextTargetJoltages, buttons, tuple(nextVisited), bestResult - i
            )
            if result + i < bestResult:
                bestResult = result + i
        else:
            if max(nextTargetJoltages) == 0:
                return i
    return bestResult


@cache
def findBestNextButton(lenTargetJoltages, buttons, visited):
    cover = calculateCover(lenTargetJoltages, buttons, visited)
    candidates = [index for index, value in enumerate(visited) if not value]

    criteria = [
        lambda index: calculateCoverScore(buttons, cover, index),
        lambda index: sum(cover[toggle] for toggle in buttons[index]),
    ]

    for criterion in criteria:
        if len(candidates) <= 1:
            break
        scored = [(criterion(j), j) for j in candidates]
        bestValue = min(s[0] for s in scored)
        candidates = [j for score, j in scored if score == bestValue]

    return candidates[0]


def calculateCoverScore(buttons, cover, j):
    buttonScore = min(cover[toggle] for toggle in buttons[j])
    return buttonScore


def calculateCover(lenTargetJoltages, buttons, visited):
    cover = [0 for _ in range(0, lenTargetJoltages)]
    for j in range(0, len(buttons)):
        if not visited[j]:
            for toggle in buttons[j]:
                cover[toggle] += 1
    return tuple(cover)


def findJoltagesCombination(targetJoltages, buttons):
    result = recurseJoltagesCombination(
        targetJoltages,
        buttons,
        tuple([False for _ in range(0, len(buttons))]),
        sum(targetJoltages),
    )
    findBestNextButton.cache_clear()
    print(result)
    return result


machines = []
with open("day10/sample.txt", "r") as file:
    for line in file:
        lights, *buttons, joltages = line.strip().split(" ")
        machines.append(
            {
                "lights": [lights[i] == "#" for i in range(1, len(lights) - 1)],
                "buttons": tuple(
                    [tuple(map(int, button[1:-1].split(","))) for button in buttons]
                ),
                "joltages": list(map(int, joltages[1:-1].split(","))),
            }
        )

t = time.process_time()
print(
    "Part 1: ",
    sum([findLightsCombination(m["lights"], m["buttons"]) for m in machines]),
)
print(
    "Part 2: ",
    sum([findJoltagesCombination(m["joltages"], m["buttons"]) for m in machines]),
)
print("(this took %0.2fs)" % (time.process_time() - t))
