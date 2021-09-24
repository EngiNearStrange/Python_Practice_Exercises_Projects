#This is a program to keep taking input from user until he gives an input greater than 100.
while(True):
    a = int(input("Please enter a number"))
    if a > 100:
        print("Congrats, you have given a correct input")
        break
    else :
        print("Incorrect input, please enter another number")