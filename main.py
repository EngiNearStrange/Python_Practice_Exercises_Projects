'''This is a comment
So leae ignore it'''
# print("I am a Mechanical Engineer")
# print("My name is Ranjeet", end=" & ")

#This is a progam to add 2 numbers
#
# print("Enter number 1")
# a = input()
# print("Enter second number")
# b = input()
# print("You entered :", a, " &", b, "& their sum is :", int(a) + int(b))

print("Please enter your age")
a = int(input())
if 5 < a < 100:
    if a > 18 :
        print("You can drive")
    elif a == 18 :
        print("Teri LOL ho gayi, you need to visit the DMV to proceed with applicaion")
    else :
        print("Sorry, you cannot drive")
else :
    print("Age is out of range")