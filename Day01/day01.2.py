import math

with open('Day01/input','r') as f: input = f.read()

total_fuel = 0
weights = [int(x) for x in input.split('\n')]
while len(weights) > 0:
    weight = weights.pop()
    fuel = math.floor(weight / 3.0) - 2
    if fuel > 0:
        total_fuel += fuel
        weights.append(fuel)

print(total_fuel)