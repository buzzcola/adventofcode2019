from shared import Machine

with open('Day09/input','r') as f: input = f.read()
codes = [int(x) for x in input.split(',')]

machine = Machine(codes)
machine.input = [1]
machine.run()
print(machine.output)

machine.reset()
machine.input.append(2)
machine.run()
print(machine.output)