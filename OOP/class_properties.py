#1. class properties, manipulation on class properties, class properties vs object properties
#2. class methods, manipulation with  class methods

# class Student_detail:
    
#     surname = "Sharma"   # class ko properties
    
#     def __init__(self,firstname):
#         self.firstname = firstname    #object ko properties
        
# s1 = Student_detail("Ram")
# print(s1.firstname)
# print(s1.surname)
# Student_detail.surname = "Gupta"
# print(s1.surname)
# s1.surname = "Yadav"
# print(s1.surname)




# Object Properties - characteristics of object, can be accessed and manipulated only by objects, these are created inside init method
# Class Properties - characteristics of classs, can be accessed and manipulated by both class and objects, these are created inside the 
#                    class but outside the init method