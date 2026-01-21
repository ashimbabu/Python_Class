"""
File handling - using python to read,write, modify the files.
Main function of file handling- open()    -> open("file_path","mode")
Opening the files in different modes:
 1. "r" - reading mode
 2. "w" - writing mode
 3. "a" - append mode
 4. "x" - create mode
 
 
 Optional :
 1. "t" - in text mode
 2. "b" - in binary mode
 
f = open("C:/Users/sigde/OneDrive/Desktop/Python/gitcommand.txt","r")
  
"""
# Reading the files:
# f = open("C:/Users/sigde/OneDrive/Desktop/Python/gitcommand.txt")
# print(f.read())
#f.close()
# with open("C:/Users/sigde/OneDrive/Desktop/Python/gitcommand.txt") as f:         # if we use 'with' keyword, we do not need to close the opened file manually
#     print(f.read())      # read - read all the contents in once
# with open("C:/Users/sigde/OneDrive/Desktop/Python/gitcommand.txt") as f:
#         print(f.readline())      # readline - read the contents of files line by line


# Writing the files:
# with open("C:/Users/sigde/OneDrive/Desktop/Python/gitcommand.txt","a") as f:   #opening the file in append mode
#     f.write("Hi I am writing this from python codes.")
    
# with open("C:/Users/sigde/OneDrive/Desktop/Python/gitcommand.txt","w") as f:    #opening the file in write mode
#     f.write("Hi I am writing this from python codes.")


# Creating the new file:
# f = open("C:/Users/sigde/OneDrive/Desktop/Python/newfile.txt","x")


#Removing the text file:
# import os
# os.remove("C:/Users/sigde/OneDrive/Desktop/Python/newfile.txt")

# if os.path.exists("C:/Users/sigde/OneDrive/Desktop/Python/newfile.txt"):
#     os.remove("C:/Users/sigde/OneDrive/Desktop/Python/newfile.txt")
# else:
#     print("File not found")