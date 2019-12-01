import math

with open('Day01/input','r') as f: input = f.read()

weights = [int(x) for x in input.split('\n')]
print(sum([math.floor(x / 3.0) - 2 for x in weights]))

