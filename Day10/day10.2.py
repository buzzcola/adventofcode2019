import shared, math

grid = shared.create_grid()
source = (22,25) # from part 1

def angle_from_top(source, target):
    vector = (target[0] - source[0], target[1] - source[1])
    return (180 - math.degrees(math.atan2(*vector))) % 360

def rank(t):
    # isn't there a better multi-key sort in python? look up back on the ground.
    between = len([x for x in shared.get_points_between(source, t) if grid[x]])
    angle = angle_from_top(source, t)
    return (between * 1000) + angle

targets = [p for p in grid if p != source and grid[p]]
targets.sort(key = rank)
solution = targets[199]
print(solution[0] * 100 + solution[1])