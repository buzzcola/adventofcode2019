from fractions import Fraction
from numpy import sign
import math
from itertools import product
import shared

grid = shared.create_grid()
max_y = int(math.sqrt(len(grid.keys())))
max_x = max_y

result = {p:0 for p in grid.keys()}

for source in product(range(0, max_x), range(0, max_y)):
    if not grid[source]: continue
    for point in product(range(0, max_x), range(0, max_y)):
        if point == source:
            continue
        
        if not grid[point]: continue

        between = [p for p in shared.get_points_between(source, point) if grid[p]]
        if len(between) == 0:
            result[source] += 1

best = max(result, key=result.get)
print('{}: {}'.format(best, result[best]))
