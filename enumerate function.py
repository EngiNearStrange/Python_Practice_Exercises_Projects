list1 = ["Ranjeet", "Riteek", "Deepa", "Laxmi", "Kajal", "Sejal"]

for index, item in enumerate(list1):
    if index%3 == 0:
        print(f"Name of {index}th user is {item}")

list2 = ["Ranjeet", "Riteek", "Deepa", "Laxmi", "Kajal", "Sejal", "Shreya", "Arya", "XYZ"]
for index, item in enumerate(list2):
    if index%3 == 0:
        print(f"Name of {index}th user is {item}.")