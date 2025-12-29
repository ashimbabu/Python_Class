# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password    #private property
        
        
# user1 = User("ram","ramram2025")
# print(user1.username, user1.__password)    #we cannot access the private property directly in such way

class User:
    def __init__(self,username,password):
        self.username = username
        self.__password = password    #private property
    
    def access_private(self):   # methods accessing  the private property
        return self.__password
        
user1 = User("ram","ramram2025")
print(user1.access_private())
