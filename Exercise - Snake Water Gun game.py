while True: #Initiating a while loop to enable infinite session plays of the game without having to run program again
    user_score = 0
    comp_score = 0
    import random #Importing random number generator module to generate a random guess for computer
    tries = 1 # Initiating with 1st try
    while tries < 11 : #Initiating a while loop for a single session with total number of tries = 10
        user_turn = int(input("Choose one of the following :\n'1' for SNAKE\n'2' for WATER\n'3' for GUN :\n"))
        ss = ["SNAKE", "WATER", "GUN"]
        comp_guess = random.choice(ss) # Generate random guess for computer and assign it to variable comp_guess
        if user_turn == 1 and comp_guess == "WATER":
            print("Computer chooses :", comp_guess, "hence you win and score a point.")
            user_score += 1 #Increment user score by 1 after user has scored a point
        elif user_turn == 1 and comp_guess == "GUN":
            print("Computer chooses:", comp_guess, "hence Computer wins and scores a point.")
            comp_score += 1 #Increment computer score by 1 after computer has scored a point
        elif user_turn == 1 and comp_guess == "SNAKE":
            print("Computer also chose :", comp_guess, "hence it is a tie, no points.")
        elif user_turn == 2 and comp_guess == "WATER":
            print("Computer chooses :", comp_guess, "hence it is a tie, no points.")
        elif user_turn == 2 and comp_guess == "GUN":
            print("Computer chooses :", comp_guess, "hence you win and score a point.")
            user_score += 1
        elif user_turn == 2 and comp_guess == "SNAKE":
            print("Computer chooses :", comp_guess, "hence Computer wins and scores a point.")
            comp_score += 1
        elif user_turn == 3 and comp_guess == "WATER":
            print("Computer chooses :", comp_guess, "hence Computer wins and scores a point.")
            comp_score += 1
        elif user_turn == 3 and comp_guess == "GUN":
            print("Computer chooses :", comp_guess, "hence it is a tie, no points.")
        elif user_turn == 3 and comp_guess == "SNAKE":
            print("Computer chooses :", comp_guess, "hence you win and score a point.")
            user_score += 1
        else :
            print("Invalid input, try again")
        tries += 1
    if user_score > comp_score:
        print("Your score is :", user_score, "and computer scored :", comp_score, "Hence you WIN. CONGRATULATIONS!!!")
    elif user_score < comp_score:
        print("Your score is :", user_score, "and computer scored :", comp_score, "Hence you LOSE. BETTER LUCK NEXT TIME!!!")
    else :
        print("Your score is :", user_score, "and computer scored :", comp_score, "Hence it is a TIE")