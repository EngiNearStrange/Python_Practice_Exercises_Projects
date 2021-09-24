class Employee:
    leaves = 22
    ML = "26  Weeks"
    def __init__(self, ename, eshift, esalary, erole, elocation, edept, egender):
        self.name = ename
        self.shift = eshift
        self.salary = esalary
        self.role = erole
        self.location = elocation
        self.dept = edept
        self.gender = egender

class Programmar(Employee):
    pass

Ranjeet = Employee("Ranjeet", "9 to 5", "22k", "Transaction processing New associate", "MDC5B", "Body", "Male")
print(Ranjeet.salary)
Ranjeet1 = Programmar("Ranjeet", "9 to 5", "22k", "Transaction processing New associate", "MDC5B", "Body", "Male")
print(Ranjeet1.role)
print(Ranjeet1.leaves)