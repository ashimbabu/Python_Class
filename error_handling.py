try:
    with open("C:/Users/acer/Desktop/Python/test.txt","r") as f:
        print(f.read())
        
except FileNotFoundError:
    print("FIle not found")
    
    
print("Program running")

