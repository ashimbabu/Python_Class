# name = {"Ram", "Shyam", "Hari"}

# Adding single data to set
# name.add("Bikash")


# Adding multiple data to set

# name.update({"Bhimesh", "Git", "Gita"})
# name.update(["Bhimesh", "Git", "Gita"])
# name.update(("Bhimesh", "Git", "Gita"))


# name.remove("Hari")
# name.discard("Ram")
# name.pop()
# name.clear()
# del name

# print(name)

# Join operation in set

# name = {"Ram", "Shyam", "Hari"}
# age = {25,34,49}
# salary = {35000,45000,55000}
# new_set = name.union(age,salary)

# new_set = name | age | salary



# Join operation using difference

name = {"Ram", "Shyam", "Hari", 34}
age = {25,34,49, "Ram"}

new_set = name.intersection(age)
new_set = name & age 
print(new_set)
