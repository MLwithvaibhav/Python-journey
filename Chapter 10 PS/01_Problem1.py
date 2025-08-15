class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Harry", "1200000", "110044")
print(p.name, p.salary, p.pin)
r = Programmer("Rohan", "120000", "660044")
print(r.name, r.salary, r.pin)