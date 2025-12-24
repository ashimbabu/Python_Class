# class Student:
#     # id = "S001"
#     # name = "Ram"      #Class ko properties
#     # contact = 9800455555
    
#     def __init__(self,id,name,contact):
#         self.id = id   # creating instance
#         self.name = name   # creating instance
#         self.contact = contact     #object ko properties
    
# s1 = Student("S001","Ram",9800)
# s2 = Student("S002","Shyam",9810)
# s3 = Student("S003","Sita",9898)
# print(s1.name,s1.id,s1.contact)
# print(s2.name,s2.id,s2.contact)
# print(s3.name,s3.id,s3.contact)


class Student:  #student class
    
    def __init__(self,id,name,contact):   # init method - it is a built-in method, it is called automatically when class is called, it sets the prooperties of object
        self.id = id   # creating instance
        self.name = name   # creating instance
        self.contact = contact     #object ko properties
    
    def details(self):  #user defined method  , we passs self parameter here because we want to access the properties of that object which called this method
        print(f"Hello, I am {self.name}. My student id is {self.id}. My contact number is {self.contact}")
        
s1 = Student("001","Ashim Babu Shrestha",9851000000)  # creating object s1
s1.details()   #calling the method details() using s1 object

s2 = Student("002","Jiban Babu Shrestha",9841000000)
s2.details()

s3 = Student("003","Nabin Babu Shrestha",9849000000)
s3.details()


#Manipulating properties of objects

# class Student:  #student class
    
#     def __init__(self,id,name,contact):
#         self.id = id   
#         self.name = name  
#         self.contact = contact     
    
#     def details(self):  
#         print(f"Hello, I am {self.name}. My student id is {self.id}. My contact number is {self.contact}")
 
# s1 = Student("S001","Ram",9800)  # creating object s1
# s1.details()   #calling the method details() using s1 object

# s1.id = "I002"    #changing the properties of s1 object
# s1.name = "Hari Krishna Maharjan"   #changing the properties of s1 object

# s1.age = 21     #adding the properties of s1 object

# del s1.contact    #deleting the properties of s1 object

# s1.details()




#Next topics :
#1. class properties, manipulation on class properties, class properties vs object properties
#2. class methods, manipulation with  class methods

