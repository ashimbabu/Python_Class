# def sum(a,b):
#     sum = a + b
#     print("Sum is :", sum)
# sum(3,5)
# sum(6,9)
# sum(10,15)
"""
Uses of function:
1. we can reuse the codes.
2. we can reduce the length of codes.
3. cades are readable when we use functions.
4. function returns the values
"""
# def sum(a,b):
#     sum_result = a + b
#     return sum_result

# result = sum(3,5)
# print("Sum is :", result)
# Rules for naming a function:
# 1. a function name should start with alphabets or underscore(_)
# 2. we can use only alphabets, numbers and underscore(_) in a function name.
# 3. we cannot give space while naming a function.

# parameters and arguments:
# def sum(a,b):    # parameters
#     sum_result = a + b
#     return sum_result
# sum(3,5) # arguments



# def greet_user(name):  # multiple times calling the function
#     print("Hello",name)
# greet_user("Ram")
# greet_user("Shyam")



# def name_details(name,country):  # multiple parameters
#     details = f"Hi, I am {name}. I am from {country}."
#     return details
    
# result = name_details("Prabin","Nepal")
# print(result)




# def greetings(name = "Girls"):  # default parameter
#     print("hello",name)
# greetings("Sita")
# greetings()
# greetings("Laxmi")


#Keyword arguments:
# Positional agruments: 
# def name_details(name,country,location):  # multiple parameters
#     details = f"Hi, I am {name}. I am from {country}. Currently, I am living in {location}"
#     return details
    
# result = name_details(location = "Kathmandu",country = "Nepal",name = "Prabin")
# print(result)
# passing dictionary(data structure) to function:
# def student_details(student):
#     print("Student id is ",student["id"])
#     print("Student name is" ,student["name"])
#     print("Student marks is" ,student["marks"])
# student = {
#     "id" : "S001",
#     "name" : "Ram",
#     "marks" : 98
# }
# student_details(student)

# Recieving list as parameter and recieving with different variable name:
# def name_list(names):
#     list_name = names
#     for i in list_name:
#         print(i)
# list_of_names = ["Ram","Shyam","Hari"]
# name_list(list_of_names)


# args and kwargs:
# def student_list(*names):
#     for i in names:
#         print(i)
# student_list("Ram","Shyam","Hari")

# def  sum_function(*num):
#     sum = 0
#     for i in num:
#         sum = sum + i
#     return sum
# result = sum_function(3,5,7,14,67,89)
# print("Sum is :", result)


