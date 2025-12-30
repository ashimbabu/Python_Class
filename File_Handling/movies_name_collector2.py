class Playlist:
    
    def __init__(self,playlist_name):
        self.playlist_name = playlist_name
        self.file_path = "C:/Users/sigde/OneDrive/Desktop/Python/FIle_Handling/movies_list.txt"
        self.movie_list = []
        self.upload_movies()
    
    def upload_movies(self):
        try:
            
            with open(self.file_path,"r") as f:
                for content in f:
                    self.movie_list.append(content.strip())
                    
        except FileNotFoundError:
            print("File not found")
                      
    def save_movie(self):
        with open(self.file_path,"a") as f:
            for content in self.movie_list:
                f.write(content)
                
    def add_movie(self,movie):
        self.movie_list.append(movie)
        self.save_movie()
        print(f"{movie} is added")
    
    def remove_movie(self,movie):
        self.movie_list.remove(movie)
        print(f"{movie} is deleted")
        
    def show_movie(self):
        print("\nYour movie list:\n")
        count = 1
        for i in self.movie_list:
            print(count,"." ,i)
            count = count + 1
            
    
print("................Movie collection App....................")
        
playlist_name = input("Enter playlist name: ")
p1 = Playlist(playlist_name)
while True:
    
    print("\nYour available options:")
    print("1. Add Movie\n2. Remove Movie\n3. Show Playlist\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        movie = input("Enter movie name to add: ")
        p1.add_movie(movie)
        
    
    elif choice == "2":
        movie = input("Enter movie name to remove: ")
        p1.remove_movie(movie)
        
    elif choice == "3":
        p1.show_movie()
        
    elif choice == "4":
        print("Exiting the app")
        break
    
    else:
        print("Invalid Choice")