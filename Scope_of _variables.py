#LEGB  - Local, Enclosing, Global, Built-in
# Local Variables - that are defined and accessed inside the function, can not be accessed outside the function
# def show():
#     x = "Ram"
#     print(x)
# show()
# GLobal Variables - that are defined outside the function, can be accessed inside or outside the function
# x = "Shyam"  
# def show():
#     x = "Ram"  # local variable
#     print(x)
# show()
# print(x)  # accessing global variable outside the function
# GLobal Keyword - to access and modify global variable inside the function
# x = "Shyam"  
# def show():
#     global x
#     x = "Ram"   
#     print(x)
# show()
# print(x)
# Enclosing Variables - variables in the enclosing function can be accessed by nested function
# def outer_function():
#     x = "Ram"
#     def inner_function():
#         print(x)
#     inner_function()
    
# outer_function()

# Built-in Variables - pre-defined variables in python that can be accessed anywhere
# print(len("Hello"))  # len is built-in function in python to find length of string