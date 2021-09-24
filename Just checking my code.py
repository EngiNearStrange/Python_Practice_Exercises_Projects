def getdate():  # defining function to capture timestamp
    import datetime
    return datetime.datetime.now()
sttime = str(getdate())

# import time #Importing time module
# import datetime #Importing datetime module
# ts = time.time()
# sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S - ')
def rohan(): #defining function to capture Rohan's data
    paramet = int(input("Press '1' to log diet & press '2' to log exercise for Rohan\n"))
    if paramet == 1:
        rohan_diet = input("What did Rohan eat today?\n")
        with open("diet_rohan.txt", "a") as drohan:
            drohan.write(sttime + rohan_diet + "\n")
    elif paramet == 2:
        rohan_exercise = input("What did Rohan do today?\n")
        with open("exercise_rohan.txt", "a") as erohan:
            erohan.write(sttime + rohan_exercise + "\n")
    else:
        print("Incorrect input")
def hamad(): #defining function to capture Hamad's data
    paramet = int(input("Press '1' to log diet & press '2' to log exercise for Hamad\n"))
    if paramet == 1:
        hamad_diet = input("What did Hamad eat today?\n")
        with open("diet_hamad.txt", "a") as dhamad:
            dhamad.write(sttime + hamad_diet + "\n")
    elif paramet == 2:
        hamad_exercise = input("What did Hamad do today?\n")
        with open("exercise_hamad.txt", "a") as ehamad:
            ehamad.write(sttime + hamad_exercise + "\n")
    else:
        print("Incorrect input")
def harry(): #defining function to capture Harry's data
    paramet = int(input("Press '1' to log diet & press '2' to log exercise for Harry\n"))
    if paramet == 1:
        harry_diet = input("What did Harry eat today?\n")
        with open("diet_harry.txt", "a") as dharry:
            dharry.write(sttime + harry_diet + "\n")
    elif paramet == 2:
        harry_exercise = input("What did Harry do today?\n")
        with open("exercise_harry.txt", "a") as eharry:
            eharry.write(sttime + harry_exercise + "\n")
    else:
        print("Incorrect input")
def logger(): #Defining the main logger tool function
    if user_name == 1:
        rohan()
    elif user_name == 2:
        hamad()
    elif user_name == 3:
        harry()
    else:
        print("Incorrect input")
# action = int(input("Do you want to log data or retrieve data?\nPress 1 to log data\nPress 2 to retrieve data\n"))
user_name = int(input("Whose data you want to capture?\nPress '1' for 'Rohan'\nPress '2' for 'Hamad'\nPress '3' for 'Harry'\n"))
logger()
# if action == 1:
#     logger()
# elif action == 2:
#     retriever()
# else:
#     print("Incorrect input")
# def retriever(): #Function to retrieve data
#     print("Nothing here")