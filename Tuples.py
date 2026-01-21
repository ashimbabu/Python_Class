name = ("Ram", "Shyam", "Hari", "Kale")

# name.remove("Mohan") # cannot change the value of tuple
# name.append("Sita")

# new_name = list(name)
# new_name.append("Sita")
# new_name2 = tuple(new_name)
# print(new_name2)

# new_name = list(name)
# new_name.remove("Ram")
# new_name2 = tuple(new_name)
# print(new_name)

# surname = ("Gupta", "Sharma", "Verma", "Giri")
# name = name + surname
# print(name)

# name = ("Ram", "Shyam", "Hari", "Kale")
# surname = ("Gupta", "Sharma", "Verma", "Giri")
# del surname
# print(name)
# print(surname)


# email = ("aaditya@gmail.com", "anish@gmail.com", "ashim@gmail.com")
# (aaditya,anish,ashim) = email # unpacking values from tuples
# print(aaditya)
# print(anish)
# print(ashim)


# email = ("aaditya@gmail.com", "anish@gmail.com", "ashim@gmail.com", "meghan@gmail.com", "rojit@gmail.com")
# (aaditya,anish,*ashim) = email # unpacking values from tuples
# print(aaditya)
# print(anish)
# print(ashim)


# name = ("Ram", "Shyam")
# name = name * 3 # Data replication inside tuples
# print(name)

name = {"Ram", "Shyam", "Hari", "Sita", "Gita"}
print(name)

"""
Lists vs Tuples:

List: 
ordered, changeable, allows duplication numbers, syntax [], methods are available, accessing the value is slow, data are secured as compared as compare tuple

Tuple:
ordered, unchangeable, allows duplication numbers, syntax (), methods are not available, accessing the value is fast, data are secured here then list

Sets:
<<<<<<< HEAD
unordered, unchangeable, doesn't allow duplication numbers, syntax {}, methods are available only for adding or removing data,

Dictionary:
ordered, unordered, changeable, doesn't allow duplication numbers, syntax {}, methods are available 
=======
unordered, unchangeable, doesn't allow duplication numbers, syntax {}, methods are not available
>>>>>>> 713c7c1577f3cf15a375fcfabfae99eafc212c95

"""