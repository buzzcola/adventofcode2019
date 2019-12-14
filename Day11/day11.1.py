from shared import Machine
with open('Day11/input','r') as f: raw = f.read()
codes = [int(x) for x in raw.split(',')]
machine = Machine(codes)

whites = set()
directions = [(0,1),(1,0),(0,-1),(-1,0)]
position = (0,0)
direction = 0
painted_positions = set()

while not machine.halted:
    machine.input.append(1 if position in whites else 0)
    while len(machine.output) < 2:
        machine.step()
    (paint_colour, rotation) = machine.output
    machine.output.clear()
    if paint_colour == 0: 
        whites.remove(position)
    else: 
        whites.add(position)
    painted_positions.add(position)
    direction = (direction + (1 if rotation == 1 else -1)) % len(directions)
    position = (position[0] + directions[direction][0], position[1] + directions[direction][1])

print(len(painted_positions))
