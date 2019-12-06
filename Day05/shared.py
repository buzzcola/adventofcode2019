from enum import Enum

class RetrieveMode(Enum):
    Position = 0
    Immediate = 1

class Opcode(Enum):
    Add = 1
    Multiply = 2
    Input = 3
    Output = 4
    JumpIfTrue = 5
    JumpIfFalse = 6
    LessThan = 7
    Equals = 8
    Halt = 99

class Machine():
    def __init__(self, codes, input):
        self.codes = codes
        self.input = input
        self.halted = False
        self.instruction_pointer = 0
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
            Opcode.Halt: 0
        }

    def step(self):
        raw = str(self._getNext(RetrieveMode.Immediate))
        self.opcode = Opcode(int(str(raw)[-2:]))
        modes = [int(x) for x in raw[0:-2].rjust(3, '0')]               
        modes.reverse()

        # override: for output parameters, always read the address using Immediate.        
        if self.opcode in (Opcode.Add, Opcode.Multiply, Opcode.LessThan, Opcode.Equals): modes[2] = 1
        elif self.opcode == Opcode.Input: modes[0] = 1
        
        for x in range(0, self.parameter_counts[self.opcode]):
            self.parameters[x] = self._getNext(RetrieveMode(modes[x]))
        
        # call the function that has the same name as the opcode.
        getattr(self, self.opcode.name)()
    
    def _getNext(self, mode):
        result = self.codes[self.instruction_pointer]
        if mode == RetrieveMode.Position:
            result = self.codes[result]
        
        self.instruction_pointer += 1
        return result

    def Add(self): self.codes[self.parameters[2]] = self.parameters[0] + self.parameters[1]
    def Multiply(self): self.codes[self.parameters[2]] = self.parameters[0] * self.parameters[1]
    def Input(self): self.codes[self.parameters[0]] = self.input
    def Output(self): print(self.parameters[0])
    def JumpIfTrue(self): 
        if self.parameters[0] != 0: self.instruction_pointer = self.parameters[1]
    def JumpIfFalse(self): 
        if self.parameters[0] == 0: self.instruction_pointer = self.parameters[1]
    def LessThan(self): self.codes[self.parameters[2]] = 1 if self.parameters[0] < self.parameters[1] else 0
    def Equals(self): self.codes[self.parameters[2]] = 1 if self.parameters[0] == self.parameters[1] else 0
    def Halt(self): self.halted = True