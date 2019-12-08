from shared import chunk
with open('Day08/input','r') as f: input = f.read()

width = 25
height = 6

pixels = [int(x) for x in input]
layers = chunk(pixels, width * height)

zero_scores = {len([x for x in layer if x == 0]): layer for layer in layers}
layer = zero_scores[min(zero_scores.keys())]

ones = len([x for x in layer if x == 1])
twos = len([x for x in layer if x == 2])
print(ones * twos)