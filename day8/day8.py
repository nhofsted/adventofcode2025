import heapq
import math


class Connection:
    def __init__(self, box1, box2):
        self.box1 = box1
        self.box2 = box2
        self.distance = sum(
            map(lambda x: pow(x, 2), map(lambda x, y: x - y, box1, box2))
        )

    def __lt__(a, b):
        return a.distance < b.distance


boxes = []
with open("day8/sample.txt", "r") as file:
    i = 0
    for line in file:
        boxes.append(tuple(map(int, line.split(","))))
        i += 1

connections = []
for i in range(0, len(boxes)):
    for j in range(0, i):
        c = Connection(boxes[i], boxes[j])
        heapq.heappush(connections, c)

circuits = set([frozenset([b]) for b in boxes])
i = 0
while connections:
    conn = heapq.heappop(connections)
    circuit1 = next(circuit for circuit in circuits if conn.box1 in circuit)
    circuit2 = next(circuit for circuit in circuits if conn.box2 in circuit)
    circuits.remove(circuit1)
    if circuit2.isdisjoint(circuit1):
        circuits.remove(circuit2)
    circuits.add(circuit1.union(circuit2))
    i += 1

    if i == 10:
        print("sample: ", math.prod(sorted(map(len, circuits))[-3:]))
    if i == 1000:
        print("part 1: ", math.prod(sorted(map(len, circuits))[-3:]))
    if len(circuits) == 1:
        print("part 2: ", conn.box1[0] * conn.box2[0])
        break
