"""This is a python program to print fibonacci series
Since Fibonacci numbers progressive value depend on last 2 numbers in the series, we denote current number
by 'c' and previous 2 numbers as 'a' and 'b' respectively wherein the value of 'b' first gets assigned to 'a',
then 'b' gets assigned the new value, i.e. last value of 'c' as they progress in the series and 'c' then gets assigned
a new value which is the sum of it's previous 2 values that are now assigned to 'a' & 'b'. The series progresses until
the condition for final value of 'c' as specified in while loop is met
"""
a = 0  # assigning the value '0' to 'a' as a start point
b = 0  # assigning the value '0' to 'b' as a start point
c = 1  # assigning 1 to c as the first number in series
while c < 10**100:
    print(c)
    a = b
    b = c
    c = a + b
