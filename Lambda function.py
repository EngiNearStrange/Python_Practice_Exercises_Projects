# def addition(a, b):
#     return a + b
# print(addition(9, 12))

# addition = lambda a, b : a + b
# print(addition(4, 5))

# def giv(lt):
#     return lt[2]


lt = [[5, 2, 7], [8, 54, 64], [5, 6, 1]]
lt.sort(key = lambda lt : lt[2])
print(lt)