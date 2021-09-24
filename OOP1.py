class Teen:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def printdetails(self):
        return f"{self.name} is {self.age} years old, weighs {self.weight} kgs and is {self.height} inches high."

    @classmethod
    def newage(cls, aage):
        cls.age = aage
        print("Teen's age has now been updated to 90 Years.")


class Old:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def printdetails(self):
        return f"{self.name} is {self.age} years old, weighs {self.weight} kgs and is {self.height} inches high."


Harry = Teen("Harry", 15, 50, 45)
Larry = Old("Larry", 60, 65, 68)
Harry.name = "Harry"
Larry.name = "Larry"
print(Harry.age)
print(Larry.age)
Harry.newage(90)
print(Larry.printdetails())
print(Harry.printdetails())
