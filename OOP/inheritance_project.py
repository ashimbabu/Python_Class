class User:
    
    def __init__(self,username,email):
        self.username = username
        self.email = email
        
    def show_details(self):
        print(f"Username : {self.username}")
        print(f"Email : {self.email}")
        
    def login_status(self):
        print("User logged in.")
        
    
class Student(User):
    
    def __init__(self,username,email,course):
       User.__init__(self,username,email) 
       self.course = course
        
    def show_details(self):       #method overriding
        User.show_details(self)
        print(f"Enrolled course: {self.course}")
        
    def login_status(self):
        print("Student logged in.")
        
    

class Admin(User):
    
    def __init__(self,username,email,access_level):
       User.__init__(self,username,email) 
       self.access_level = access_level
        
    def show_details(self):       #method overriding
        User.show_details(self)
        print(f"Access level: {self.access_level}")
        
    def login_status(self):
        print("Admin logged in.")  


users = []
while True:
    
    print("\nYour available options:")
    print("1. Add Student\n2. Add Admin\n3. Show All Users\n4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1 :
        username = input("Enter username: ")
        email = input("Enter email: ")
        course = input("Enter course: ")
        users.append(Student(username,email,course))
        
    elif choice == 2 :
        username = input("Enter username: ")
        email = input("Enter email: ")
        access_level = input("Enter access_level: ")
        users.append(Admin(username,email,access_level))
        
    elif choice == 3:
        print("All Users Details:")
        for i in users:
            i.show_details()
            i.login_status()
    else:
        print("Exited")
        break