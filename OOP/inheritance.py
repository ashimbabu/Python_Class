# accessing the methods of parent class from the object of child class
class User:
    
    def __init__(self,firstname,surname):
        
        self.firstname = firstname
        self.surname = surname
    
    def show_details(self):
        print(f"Hi, I am {self.firstname} {self.surname}")
    
class Student(User):     # This is a child class of parent class(User)
    pass
obj2 = Student("Ram","Yadav")
obj2.show_details()


# init method in child class
class User:
    
    def __init__(self,firstname,surname):
        
        self.firstname = firstname
        self.surname = surname
    
    def show_details(self):
        print(f"Hi, I am {self.firstname} {self.surname}")
    

class Student(User):     # This is a child class of parent class(User)
    
    def __init__(self,firstname,surname):
        User.__init__(self,firstname,surname)     #inherited from parent class
        # super().__init__(firstname,surname)
        
obj2 = Student("Ram","Yadav")
obj2.show_details()


class User:
    
    def __init__(self,firstname,surname):
        self.firstname = firstname
        self.surname = surname
    
    def show_details(self):
        print(f"Hi, I am {self.firstname} {self.surname}")
    
class Student(User):    
    
    def __init__(self,firstname,surname,symbol_num,year,division):
        User.__init__(self,firstname,surname)
        self.symbol_num = symbol_num 
        self.year = year
        self.division = division
           
    def congrats_message(self):
        print(f"Congratulation! Mr. {self.firstname} {self.surname} \nYOu have been passed out with {self.division} division.\nYour registration number is {self.symbol_num}.\nYour passed out year is {self.year}")
        
obj2 = Student("Ashim Babu","Shrestha",25969584,2077,"1st")
obj2.congrats_message()