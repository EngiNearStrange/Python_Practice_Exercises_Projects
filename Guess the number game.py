n = 18
#Write a program to make user guess the number and for every wrong guess, give hint and not more than 10 guesses
a = 1
while a<11:
    b = int(input("Guess the number : \n"))
    if b == n:
        print("You are correct, the number is", n, "You guessed it in", a, "attempts.")
        break
    elif b < n:
        print("No, the actual number is greater than ", b)
        print("Number of guesses used :", a, ", you have", 10 - a, "guesses left")
    else:
        print("No, the actual number is lesser than ", b)
        print("Number of guesses used :", a, ", you have", 10 - a, "guesses left")
    if a == 9:
        print("This is the last chance")
    elif a == 10:
        print("Game Over")
        break
    a = a + 1