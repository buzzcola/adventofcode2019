from itertools import product

with open('Day02/input','r') as f: input = f.read()
start_codes = [int(x) for x in input.split(',')]
magic_number = 19690720

def compute(codes, noun, verb):
    position = 0
    codes[1] = noun
    codes[2] = verb
    while codes[position] != 99:
        (opcode, a, b, c) = codes[position:position+4]
        if opcode == 1: codes[c] = codes[a] + codes[b]
        else: codes[c] = codes[a] * codes[b]
        position += 4
    
    return codes[0]

for (noun, verb) in product(range(0,99), range(0,99)):
    codes = start_codes.copy()
    result = compute(codes, noun, verb)
    if result == magic_number:
        print((100 * noun) + verb)
        break