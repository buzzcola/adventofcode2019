with open('Day02/input','r') as f: input = f.read()
codes = [int(x) for x in input.split(',')]
codes[1] = 12
codes[2] = 2

position = 0

while codes[position] != 99:
    (opcode, a, b, c) = codes[position:position+4]
    if opcode == 1: codes[c] = codes[a] + codes[b]
    else: codes[c] = codes[a] * codes[b]
    position += 4

print(', '.join(map(str, codes)))