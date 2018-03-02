class Dog:
    name = ''
    def bark(self):
        m = self.name + ': Bow wow'
        print m
pochi = Dog()
pochi.name = 'Pochi'
pochi.bark()


class Calculation:
    value = 0
    def square(self):
        s = self.value * self.value
        return s

calcs = [Calculation(), Calculation(), Calculation()]
calcs[0].value = 3
calcs[1].value = 5
calcs[2].value = 6

for c in calcs:
    print c.square()
