#This is a program to take input from user and keep taking input as long as it is less than 100
a = int(input("Please enter the number"))
'''Making this a comment to access program laer if reqd
while (a<100):
    print("Number is less than 100")
    a = int(input("Enter another number"))
    if a == 100:
        print("Thank you for entering the correct number")'''

while (True):
    if a<100:
        a = int(input("Does not meet criteria, please enter another number that is greater than 100"))
        continue
    print("Thank you for giving a proper input")
    break