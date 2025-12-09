corners = []
with open("day9/sample.txt", "r") as file:
    for line in file:
        corners.append(tuple(map(int, line.split(","))))

maxArea = 0
for i in range(0, len(corners)):
    for j in range(0, i):
        maxArea = max(
            maxArea,
            (abs(corners[i][0] - corners[j][0]) + 1)
            * (abs(corners[i][1] - corners[j][1]) + 1),
        )

print("part 1: ", maxArea)

maxArea = 0
for i in range(0, len(corners)):
    for j in range(0, i):
        # is potential area bigger?
        area = (abs(corners[i][0] - corners[j][0]) + 1) * (
            abs(corners[i][1] - corners[j][1]) + 1
        )
        if area <= maxArea:
            continue

        b = min(corners[i][1], corners[j][1])
        t = max(corners[i][1], corners[j][1])
        l = min(corners[i][0], corners[j][0])
        r = max(corners[i][0], corners[j][0])

        # check if polygon crosses
        stop = False
        for k in range(0, len(corners)):
            x = corners[k][0]
            y = corners[k][1]
            prevX = corners[k - 1][0]
            prevY = corners[k - 1][1]
            crossTop = prevX > l and prevX < r and prevY >= t and y < t
            crossBottom = prevX > l and prevX < r and prevY <= b and y > b
            crossRight = prevY > b and prevY < t and prevX >= r and x < r
            crossLeft = prevY > b and prevY < t and prevX <= l and x > l
            if crossTop or crossBottom or crossRight or crossLeft:
                stop = True
                break
        if stop:
            continue

        # check if we're inside the polygon
        if t > b + 1:
            scanLine = b + 1
            inside = False
            for k in range(0, len(corners)):
                y1 = corners[k - 1][1]
                y2 = corners[k][1]
                x = corners[k][0]
                if y1 > y2:
                    y1, y2 = y2, y1
                elif y1 == y2:
                    continue
                if y1 <= scanLine and y2 >= scanLine and x <= l:
                    inside = not inside
            if not inside:
                continue

        # we're the new champion
        maxArea = area

print("part 2: ", maxArea)
