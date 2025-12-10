numbers = [1,2,3,4,5,6,7,8,9,10]

# square_list = [i**2 for i in numbers]
# cube_list = [i**3 for i in numbers]
# print(square_list)
# print(cube_list)

# even_numbers = [i for i in numbers if i%2 ==0]
# odd_numbers = [i for i in numbers if i%2 != 0]
# print(even_numbers)
# print(odd_numbers)

# numbers = [1,2,-4,-7,6,9,-9,5]
# newlist = [i for i in numbers if i>=0]
# newlist.sort()
# newlist.sort(reverse=True)
# print(newlist)

birds = ["Sparrow", "Eagle", "Parrot", "Pigeon", "Peacock", "Owl"]
newlist = [i.upper() for i in birds]
newlist2 = [i.lower() for i in birds]
print(newlist)
print(newlist2)
