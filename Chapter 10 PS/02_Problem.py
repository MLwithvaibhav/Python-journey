class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of given number is: {self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot of given number is: {self.n**1/2}")
    def cube(self):
        print(f"The cube of given number is: {self.n*self.n*self.n}")


a = Calculator(4)
a.square()
a.squareroot()
a.cube()

