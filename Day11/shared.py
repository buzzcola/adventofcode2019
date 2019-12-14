from enum import Enum

class RetrieveMode(Enum):
    Position = 0
    Immediate = 1
    Relative = 2
    RelativeImmediate = 3

class Opcode(Enum):
    Add = 1
    Multiply = 2
    Input = 3
    Output = 4
    JumpIfTrue = 5
    JumpIfFalse = 6
    LessThan = 7
    Equals = 8
    AdjustRelativeBase = 9
    Halt = 99

class Machine():
    def __init__(self, codes, name = ""):
        self.name = name
        self.codes_backup = {i:codes[i] for i in range(len(codes))}
        self.codes = self.codes_backup.copy()
        self.input = []
        self.output = []
        self.halted = False
        self.instruction_pointer = 0
        self.relative_base = 0
        self.raw = ''
        self.opcode = 0
        self.parameters = [0,0,0]
        self.parameter_counts = {
            Opcode.Add: 3,
            Opcode.Multiply: 3,
            Opcode.Input: 1,
            Opcode.Output: 1,
            Opcode.JumpIfTrue: 2,
            Opcode.JumpIfFalse: 2,
            Opcode.LessThan: 3,
            Opcode.Equals: 3,
            Opcode.AdjustRelativeBase: 1,
            Opcode.Halt: 0
        }

    def readMemory(self, i):
        return self.codes[i] if i in self.codes else 0
    
    def writeMemory(self, i, value):
        self.codes[i] = value
    
    def run(self, until = None):
        while not self.halted and (until == None or not until()):
            self.step()

    def step(self):
        self.raw = str(self._getNext(RetrieveMode.Immediate))
        self.opcode = Opcode(int(str(self.raw)[-2:]))
        modes = [int(x) for x in self.raw[0:-2].rjust(3, '0')]               
        modes.reverse()

        # override: for output parameters, always read the address using Immediate.        
        if self.opcode in (Opcode.Add, Opcode.Multiply, Opcode.LessThan, Opcode.Equals) and modes[2] == 2: modes[2] = 3
        elif self.opcode in (Opcode.Add, Opcode.Multiply, Opcode.LessThan, Opcode.Equals): modes[2] = 1
        elif self.opcode == Opcode.Input and modes[0] == 2: modes[0] = 3
        elif self.opcode == Opcode.Input: modes[0] = 1
        
        for x in range(0, self.parameter_counts[self.opcode]):
            self.parameters[x] = self._getNext(RetrieveMode(modes[x]))
        
        # call the function that has the same name as the opcode.
        #self.debug()
        getattr(self, self.opcode.name)()
        self.parameters = [None, None, None]
    
    def _getNext(self, mode):
        result = self.readMemory(self.instruction_pointer)
        if mode == RetrieveMode.Position:
            result = self.readMemory(result)
        elif mode == RetrieveMode.Relative:
            result = self.readMemory(result + self.relative_base)
        elif mode == RetrieveMode.RelativeImmediate:
            result = result + self.relative_base
        
        self.instruction_pointer += 1
        return result

    def debug(self):
        print("{s.raw} {s.name}: {s.opcode.name} {s.parameters} i:{s.input} o:{s.output} rb:{s.relative_base}".format(s = self))

    def reset(self):
        self.codes = self.codes_backup.copy()
        self.input.clear()
        self.output.clear()
        self.instruction_pointer = 0
        self.relative_base = 0
        self.halted = False
        self.opcode = None
        self.parameters = [0,0,0]

    def Add(self): self.writeMemory(self.parameters[2], self.parameters[0] + self.parameters[1])
    def Multiply(self): self.writeMemory(self.parameters[2], self.parameters[0] * self.parameters[1])
    def Input(self): self.writeMemory(self.parameters[0], self.input.pop(0))
    def Output(self): self.output.append(self.parameters[0])
    def JumpIfTrue(self): 
        if self.parameters[0] != 0: self.instruction_pointer = self.parameters[1]
    def JumpIfFalse(self): 
        if self.parameters[0] == 0: self.instruction_pointer = self.parameters[1]
    def LessThan(self): self.writeMemory(self.parameters[2], 1 if self.parameters[0] < self.parameters[1] else 0)
    def Equals(self): self.writeMemory(self.parameters[2], 1 if self.parameters[0] == self.parameters[1] else 0)
    def AdjustRelativeBase(self): self.relative_base += self.parameters[0]
    def Halt(self): self.halted = True