from shared import Moon
import itertools as it
import numpy as np

with open('Day12/input','r') as f: raw = f.read()
moons = [Moon(*[int(c.split('=')[1]) for c in line[1:-1].split(',')]) for line in raw.split('\n')]
moon_pairs = [list(x) for x in it.combinations(moons, 2)]

def hash_moons(moons, dimension):
    return hash(';'.join([str(moon.position[dimension]) + ',' + str(moon.velocity[dimension]) for moon in moons]))

solutions = [None, None, None]
seen = [set() for _ in range(3)]
for dimension in range(3):
    seen[dimension].add(hash_moons(moons, dimension))

step = 0
while any([x == None for x in solutions]):
    for (dimension, moon_pair) in it.product([0,1,2], moon_pairs):
        if moon_pair[0].position[dimension] == moon_pair[1].position[dimension]: continue
        moon_pair.sort(key=lambda x: x.position[dimension])
        moon_pair[0].velocity[dimension] += 1
        moon_pair[1].velocity[dimension] -= 1
    for (dimension, moon) in it.product([0,1,2], moons):
        moon.position[dimension] += moon.velocity[dimension]
    
    step += 1
    for dimension in range(3):
        if solutions[dimension]: continue
        h = hash_moons(moons, dimension)
        if h in seen[dimension]: solutions[dimension] = step
        seen[dimension].add(h)
    
print(np.lcm.reduce(solutions, dtype='int64'))