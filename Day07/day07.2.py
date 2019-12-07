from shared import Machine
import itertools as it

with open('Day07/input','r') as f: input = f.read()
codes = [int(x) for x in input.split(',')]

machines = [Machine(codes, name) for name in ["A","B","C","D","E"]]
outputs = []

for phases in it.permutations([5,6,7,8,9]):

    last_machine = None
    for (machine, phase) in zip(machines, phases): machine.input.append(phase)

    for machine in it.cycle(machines):
        last_output = 0 if not last_machine else last_machine.output.pop()
        machine.input.append(last_output)
        machine.run(until = lambda: machine.output)
        last_machine = machine
        if machine.halted:
            outputs.append(last_output)
            break
    
    for machine in machines:
        machine.reset()

print(max(outputs))