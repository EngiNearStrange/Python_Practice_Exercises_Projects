def markss(*args):
    stname = input("Whose marks do you want to see?")
    stname.uppercase()
    print("Marks for the students are :")
    for item in args:
        print(item[stname])
# marks = ["Harry", "Ranjeet", "Riteek"]
from marklist import marks as mlt
markss(*mlt)