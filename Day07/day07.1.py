from shared import Machine
import itertools as it

with open('Day07/input','r') as f: input = f.read()
codes = [int(x) for x in input.split(',')]

machines = [Machine(codes) for _ in range(5)]
outputs = []
for phases in it.permutations(range(5)):
    input = 0
    for i in range(5):
        machines[i].input = [phases[i], input]
        machines[i].run()
        input = machines[i].output[0]
        
    outputs.append(machines[-1].output[0])
    for i in range(5):
        machines[i].reset()

print(max(outputs))