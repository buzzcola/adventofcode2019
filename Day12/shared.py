class Moon:
    def __init__(self, x, y, z):
        self.position = [x,y,z]
        self.velocity = [0,0,0]
    
    def __str__(self):
        return 'p:{0}\t\tv:{1}\t\tte:{2}'.format(self.position, self.velocity, self.total_energy())
      
    def kinetic_energy(self):
        return sum([abs(x) for x in self.velocity])

    def potential_energy(self):
        return sum([abs(x) for x in self.position])

    def total_energy(self):
        return self.kinetic_energy() * self.potential_energy()