#####################    MAP     #########################
list1 = [2, 5, 6, 2, 1, 7, 8, 3, 5, 9, 11, 51, 2, 1, 0, 63]
#
# # for item in range(len(list1)):
# #     list1[item] = list1[item]*list1[item]
#
# # def cube(a):
# #     return a*a*a
#
list2 = list(map(lambda a: a*a*a*a, list1))
print(list2)

#####################    FILTER     #########################

def lsthan9(num):
    return num<9
lessthan9 = list(filter(lsthan9, list1))
print(lessthan9)

#####################    REDUCE     #########################

from functools import reduce
# num = 0
# for item in list1:
#     num = num + item
# print(num)
sumnum = reduce(lambda x, y: x + y, list1)
print(sumnum)