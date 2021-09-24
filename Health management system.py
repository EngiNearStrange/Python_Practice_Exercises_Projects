def getdate():  # defining function to capture timestamp
    import datetime
    return datetime.datetime.now().strftime('%d-%m-%y__%H:%M:%S - ')
sttime = str(getdate())

# import time #Importing time module
# import datetime #Importing datetime module
# ts = time.time()
# sttime = datetime.datetime.fromtimestamp(ts)

def rohan(): #defining function to capture Rohan's data
    paramet = int(input("Press '1' to log diet & press '2' to log exercise for Rohan\n"))
    if paramet == 1:
        rohan_diet = input("What did Rohan eat today?\n")
        with open("diet_rohan.txt", "a") as drohan:
            drohan.write(sttime + rohan_diet + "\n")
        print(rohan_diet, " has been added to Rohan's diet log successfully.")
    elif paramet == 2:
        rohan_exercise = input("What did Rohan do today?\n")
        with open("exercise_rohan.txt", "a") as erohan:
            erohan.write(sttime + rohan_exercise + "\n")
        print(rohan_exercise, " has been added to Rohan's exercise log successfully.")
    else:
        print("Incorrect input")

def hamad(): #defining function to capture Hamad's data
    paramet = int(input("Press '1' to log diet & press '2' to log exercise for Hamad\n"))
    if paramet == 1:
        hamad_diet = input("What did Hamad eat today?\n")
        with open("diet_hamad.txt", "a") as dhamad:
            dhamad.write(sttime + hamad_diet + "\n")
        print(hamad_diet, " has been added to Hamad's diet log successfully.")
    elif paramet == 2:
        hamad_exercise = input("What did Hamad do today?\n")
        with open("exercise_hamad.txt", "a") as ehamad:
            ehamad.write(sttime + hamad_exercise + "\n")
        print(hamad_exercise, " has been aded Hamad's exercise log successfully.")
    else:
        print("Incorrect input")

def harry(): #defining function to capture Harry's data
    paramet = int(input("Press '1' to log diet & press '2' to log exercise for Harry\n"))
    if paramet == 1:
        harry_diet = input("What did Harry eat today?\n")
        with open("diet_harry.txt", "a") as dharry:
            dharry.write(sttime + harry_diet + "\n")
        print(harry_diet, " has been added to Harry's diet log successfully.")
    elif paramet == 2:
        harry_exercise = input("What did Harry do today?\n")
        with open("exercise_harry.txt", "a") as eharry:
            eharry.write(sttime + harry_exercise + "\n")
        print(harry_exercise, " has been added to Harry's exercise log successfully.")
    else:
        print("Incorrect input")

def ret_rohan(): #Defining function to retrieve Rohan's data
    ret_paramet = int(input("What data you want to see?\nPress '1' for diet and '2' for exercise : \n"))
    if ret_paramet == 1:
        with open("diet_rohan.txt") as drohan:
            drohan_data = drohan.readlines()
            for item in drohan_data:
                print(item)
    elif ret_paramet == 2:
        with open("exercise_rohan.txt") as erohan:
            erohan_data = erohan.readlines()
            for item in erohan_data:
                print(item)

def ret_hamad(): #Defining function to retrieve Hamad's data
    ret_paramet = int(input("What data do you wat to see?\nPress '1' for diet, '2' for exercise :\n"))
    if ret_paramet == 1:
        with open("diet_hamad.txt") as dhamad:
            dhamad_data = dhamad.readlines()
            for item in dhamad_data:
                print(item)
    elif ret_paramet == 2:
        with open("exercise_hamad.txt") as ehamad:
            ehamad_data = ehamad.readlines()
            for item in ehamad_data:
                print(item)
    else :
        print("Invalid input")

def ret_harry(): #Defining function to retrieve Harry's data
    ret_paramet = int(input("What data do you want to see?\nPress '1' for diet & '2' for exercise :\n "))
    if ret_paramet == 1:
        with open("diet_harry.txt") as dharry:
            dharry_data = dharry.readlines()
            for item in dharry_data:
                print(item)
    elif ret_paramet == 2:
        with open("exercise_harry.txt") as eharry:
            eharry_data = eharry.readlines()
            for item in eharry_data:
                print(item)
    else :
        print("Invalid input")

def logger(): #Defining the function to log client data
    user_name = int(input("Whose data you want to capture?\nPress '1' for 'Rohan'\nPress '2' for 'Hamad'\nPress '3' for 'Harry'\n"))
    if user_name == 1:
        rohan()
    elif user_name == 2:
        hamad()
    elif user_name == 3:
        harry()
    else:
        print("Incorrect input")

def retriever(): #Defining the function to retrieve client data
    ret_name = int(input("Whose data do you want to see?\nPress '1' for Rohan\nPresss '2' for Hamad\nPress '3' for Harry\n"))
    if ret_name == 1:
        ret_rohan()
    elif ret_name == 2:
        ret_hamad()
    elif ret_name == 3:
        ret_harry()
    else:
        print("Invalid input")

while True:
    initiater = int(input("Do you want to log data or do you want to retrieve data?\nPress '1' to log\nPress '2' to retrieve\n"))
    if initiater == 1:
        logger()
    elif initiater == 2:
        retriever()
    else:
        print("Invalid input")