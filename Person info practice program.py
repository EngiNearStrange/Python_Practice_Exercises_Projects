#This is a program wherein one can access someones details just by entering their name
detail_1 = {"amma" : 1960, "laxmi":1984, "ranjeet":1991, "deepa":1990, "riteek":2000, "kajal":2005, "sejal":2007, "shreya":2012, "aarya":2017}
while(True):
    name = input("Enter a name: ")
    if name in detail_1:
        print("Was born in the year : ", detail_1[name])
        continue
    else:
        print("Get lost")
        break