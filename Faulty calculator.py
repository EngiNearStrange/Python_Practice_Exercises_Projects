
"""This is a program to build a faulty calculator which does all operations correctly except 45*3=555, 56+9=77, 56/6=4
Program will take operator and two numbers as input from user and give an output"""
while(True):
    i_op = input("What operation do you want to perform? +, -, *, / \n")
    i_num1 = int(input("Enter first number :\n"))
    i_num2 = int(input("Enter second number : \n"))
    if i_num1 == 45 and i_num2 == 3 and i_op == '*' :
        print("The answer is : 555")
    elif i_num1 == 56 and i_num2 == 9 and i_op == '+' :
        print("The answer is : 77")
    elif i_num1 == 56 and i_num2 == 6 and i_op == '/' :
        print("The answer is : 4")
    elif i_op == '+' :
        print("The sum of two numbers is :", i_num1 + i_num2)
    elif i_op == '-' :
        print("The difference is :", i_num1 - i_num2)
    elif i_op == '*' :
        print("The product of these two numbers is :", i_num1 * i_num2)
    elif i_op == '/' :
        print("The division gives :", i_num1 / i_num2)