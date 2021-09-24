#This is a program to demonstrate exception handling in Python
try:
    a = input("Enter number 1 :\n")
    b = input("Enter number 2 :\n")
    print("The sum of these two numbers is :", int(a) + int(b))
except Exception as e:
    print(e)
print("This is an important activity")