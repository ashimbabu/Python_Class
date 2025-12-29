class Human:
    def __init__(self,species,features):
        self.species = species
        self.features = features
        
    def show_details(self):
        print(f"This is Human class. It has species as {self.species} and features as {self.features}")

class Reptiles:
    def __init__(self,species,features):
        self.species = species
        self.features = features
        
    def show_details(self):
        print(f"This is Reptiles class. It has species as {self.species} and features as {self.features}")
         
    
class Birds:
    def __init__(self,species,features):
        self.species = species
        self.features = features
        
    def show_details(self):
        print(f"This is Birds class. It has species as {self.species} and features as {self.features}")
        
human1 = Human("Human","walk")
rep1 = Reptiles("Reptile","crawl")
bird1 = Birds("Bird","fly")

for i in (human1,rep1,bird1):
    i.show_details()