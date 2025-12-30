# lambda arguments : expressions
# num = lambda x : x + 20
# result = num(5)
# print("Result is :", result)

# num = lambda x : x ** 2
# result = num(5) 
# print("Result is :", result)

# num = lambda x,y : x + y
# result = num(5,3) 
# print("Result is :", result)

# num = lambda x,y,z : x + y * z
# result = num(5,3,2) 
# print("Result is :", result)

def multiply(num1):
    # product = lambda num2 : num1 * num2  # -> lambda num2 : 5 * num2
    # return product
    return lambda num2 : num1 * num2   # lambda num2 : 5 * 4
result = multiply(5)
final_result = result(4)
print(final_result)


def cube(x):
    result = lambda y : x ** y   #-> lambda y : 5 ** y
    return result  # lambda y : 5 ** 3 
result = cube(5)
cube_result = result(3)
print(cube_result)



