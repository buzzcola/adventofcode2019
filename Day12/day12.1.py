from shared import Moon
import itertools as it

with open('Day12/input','r') as f: raw = f.read()
moons = [Moon(*[int(c.split('=')[1]) for c in line[1:-1].split(',')]) for line in raw.split('\n')]
moon_pairs = [list(x) for x in it.combinations(moons, 2)]

for step in range(0, 1000):
    for (dimension, moon_pair) in it.product([0,1,2], moon_pairs):
        if moon_pair[0].position[dimension] == moon_pair[1].position[dimension]: continue
        moon_pair.sort(key=lambda x: x.position[dimension])
        moon_pair[0].velocity[dimension] += 1
        moon_pair[1].velocity[dimension] -= 1
    for (dimension, moon) in it.product([0,1,2], moons):
        moon.position[dimension] += moon.velocity[dimension]
    
total_energy = sum([m.total_energy() for m in moons])
print('Total energy: {}'.format(total_energy))