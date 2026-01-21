"""

OOP- Object Oriented Programming

Uses - 
1. Clean and clear Structure
2. Reuse of codes
3. Easy to maintain
4. Easy to debug
5. DRY concept (Dont repeat yourself)
6. Application development

We use class keyword while creating the class.

Class: collections of objects
Object: is used to access the codes/functions/logics of class

Characteristics of OOP:
1. Inheritance : to implement the properties of parent class into its child class
2. Encapsulation : the binding of data and methods
3. Abstraction : giving access of only essential data to user, hiding the implementation details
4. Polymorphism : single interface, but many implementations; same method but behaves differently
5. Reusability : created once, it can be reused accross multiple programs
6. Message Passing :  parameters, objects

"""

class calculation:
    def show(x,y,z):
        pass
    name = "Ashim"
    
obj1 = calculation()
print(obj1.name)

obj2 = calculation()
obj3 = calculation()

print(obj2.name)
print(obj3.name)

# del obj1
# print(obj1.name)


# init method
# self
# multiple parameter
# accessing properties using self
# properties
