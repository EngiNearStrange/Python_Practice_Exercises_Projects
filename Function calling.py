def test_func() :
    print("You have successfully called a function named test_func for :", a, "th time")
a = int(input("Enter a number :\n"))
while(a < 90):
    test_func()
    a += 1