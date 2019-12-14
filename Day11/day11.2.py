from shared import Machine
import itertools

with open('Day11/input','r') as f: raw = f.read()
codes = [int(x) for x in raw.split(',')]
machine = Machine(codes)

whites = set()
directions = [(0,1),(1,0),(0,-1),(-1,0)]

position = (0,0)
direction = 0
whites.add(position)

while not machine.halted:
    machine.input.append(1 if position in whites else 0)
    while len(machine.output) < 2:
        machine.step()
    (paint_colour, rotation) = machine.output
    machine.output.clear()
    if paint_colour == 0: 
        if position in whites: whites.remove(position)
    else: 
        whites.add(position)
    direction = (direction + (1 if rotation == 1 else -1)) % len(directions)
    position = (position[0] + directions[direction][0], position[1] + directions[direction][1])

(min_x, max_x, min_y, max_y) = (0,0,0,0)
for point in whites:
    (min_x, max_x) = (min(min_x, point[0]), max(max_x, point[0]))
    (min_y, max_y) = (min(min_y, point[1]), max(max_y, point[1]))

for y in range(max_y, min_y-1, -1):
    for x in range(min_x, max_x + 1):
        print('X' if (x,y) in whites else ' ', end='')
    print()