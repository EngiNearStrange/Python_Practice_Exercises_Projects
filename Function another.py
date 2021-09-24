def func1(a, b):
    """This is a function to print product of two numbers"""
    product = a * b
    print("Product of A & B is :", product)
    return product
l = func1(55, 6)
print(l)
print(func1.__doc__)