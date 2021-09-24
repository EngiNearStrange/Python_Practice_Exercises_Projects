#This is a program to print all items from a list
a = ['a', 'b', 6, 9, 10, 11.2, "focl", 9.362, 15, 'Ranjeet', "Shreya", "Kajal", "Riteek"]
# a = [1,7,3,9,20.5,16.55,5.5]
for i in a:
    if type(i) == int or type(i) == float and i > 6:
        print(i)