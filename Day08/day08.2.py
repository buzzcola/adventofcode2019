from shared import chunk
with open('Day08/input','r') as f: input = f.read()

width = 25
height = 6
layer_size = width * height

pixels = [int(x) for x in input]
layers = chunk(pixels, layer_size)
columns = [[layer[i] for layer in layers] for i in range(layer_size)]

for i in range(0, layer_size):
    pixel = next(filter(lambda x: x != 2, columns[i]))
    print(' ' if pixel == 0 else 'X', end='')    
    if (i+1) % width == 0: print()