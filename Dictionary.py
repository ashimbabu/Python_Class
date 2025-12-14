"""
Lists vs Tuples:

List: 
ordered, changeable, allows duplication numbers, syntax [], methods are available, accessing the value is slow, data are secured as compared as compare tuple

Tuple:
ordered, unchangeable, allows duplication numbers, syntax (), methods are not available, accessing the value is fast, data are secured here then list

Sets:
unordered, unchangeable, doesn't allow duplication numbers, syntax {}, methods are available only for adding or removing data,

Dictionary:
ordered, unordered, changeable, doesn't allow duplication numbers, syntax {}, methods are available 

"""

# car = {
#     "brand" : "toyata",
#     "color" : ["black","White","red"],
#     "model" : "2025",
#     "price" : 20000000
    
# }

# print(car)

# dictionary variable = { key : value }


# Accessing the values from dictionary

# a = ["brand"]
# b = ["color"]
# print(a)
# print(b)

# a = car.get("brand")
# b = car.get("price")
# print(a)
# print(b)

# a = car.keys()
# print(a)
# b = car.values()
# print(b)

# changine values of dictionary

# car["model"] = 2027
# car["price"] = 50000000
# print(car)

# Using update() method to change the values of dictionary

# car = {
    
#     "brand" : "toyata",
#     "color" : ["black","White","red"],
#     "model" : "2025",
#     "price" : 20000000
    
    
# }

# car.update({"brand" : "tesla", "model" : 2026, "color" : ["black", "red", "blue", "brown"]})
# car.update({"enginetype" : "electric"})
# print(car)

# Removing data from dictionary:

# car = {
    
#     "brand" : "toyata",
#     "color" : ["black","White","red"],
#     "model" : "2025",
#     "price" : 20000000
    
    
# }

# using the pup() method to remove the specific items from dictionary

# car.pop("color")

# using pupitem() method to remove the last inserted item from dictionary

# car.popitem()

# using del keyword to remove specific item from dictionary
# del car["model"]
# car.clear()
# print(car)

# Iteration through dictionary
# car = {
    
#     "brand" : "toyata",
#     "color" : ["black","White","red"],
#     "model" : "2025",
#     "price" : 20000000
    
    
# }

# for i in car:
#     print(car)
    
# for i in car:
#     print(car[i])

# for i in car.keys():
#     print(i)

# for i in car.values():
#     print(i)

# for i,j in car.items():
#     print(i,j)

# Nasted Dictionary

# car1 = { "brand" : "toyata", "color" : "black", "model" : 2025, "price" : 200000 }
# car2 = { "brand" : "tesla", "color" : "white", "model" : 2026, "price" : 300000 }
# car3 = { "brand" : "bmw", "color" : "red", "model" : 2027, "price" : 400000 }

# cars = {
#     "car1st": car1,
#     "car2nd": car2,
#     "car3rd": car3
# }
# print(cars)

# cars = {
#     "car1": { "brand" : "toyata", "color" : "black", "model" : 2025, "price" : 200000 },
#     "car2": { "brand" : "tesla", "color" : "white", "model" : 2026, "price" : 300000 },
#     "car3": { "brand" : "bmw", "color" : "red", "model" : 2027, "price" : 400000 }

# }

# # print(cars)

# # print(cars["car3"])

# print(cars["car3"] ["brand"])
# print(cars["car3"] ["color"])
