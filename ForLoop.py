name = ["Ram", "Shyam", "Mohan", "Sohan"]

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# For Loop -> iteration

# for i in name:
#     print(i)
    
# cars ["BMW", "Audi", "Ferrari", "Lamborghini"]
# for i in cars:
#     print(i)
    
# data = "Python"
# for i in data:
#     print(i)

# Range Function:
# for i in range(5):
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(1,11,3):
#     print(i)
    
# sum = 0
# for i in range(1,10):
#     sum = sum + i
#     print(sum)

for i in range(5): # i loop
    for j in range(3): # j loop
        print("*", end=" ")
    print("\n")
    

for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print("\n")


for i in range(10,0,-1):
    print(i)