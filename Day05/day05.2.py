from shared import Machine

with open('Day05/input','r') as f: input = f.read()
codes = [int(x) for x in input.split(',')]
machine = Machine(codes, 5)
while not machine.halted:
    machine.step()