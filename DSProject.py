# student_details = []
# while = True:
# print("Student Management System")
# print("Your availabe options:")
# print("1. Add Student") # id, name, marks
# print("2. View Students")
# print("3. Passed Students")
# print("4. Exit")
# choice = input("Enter your choice: ")

# if choice == "1" :
#     std_id = input("Enter student ID :")
#     std_name = input("Enter your name :")
#     std_marks = int(input("Enter student marks :"))
#     student = {
        
#         "id" : std_id, 
#         "name" : std_name, 
#         "marks" : std_marks
#     }
#     student_details.append(student)
#     print("Student added successfully!")
    
    
    
    
# student_details = []
# while True:
#     print("Student Management System")
#     print("Your availabe options:")
#     print("1. Add Student") # id, name, marks
#     print("2. View Students")
#     print("3. Passed Students")
#     print("4. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1" :
#         std_id = input("Enter student ID :")
#         std_name = input("Enter your name :")
#         std_marks = int(input("Enter student marks :"))
#         student = {
            
#             "id" : std_id, 
#             "name" : std_name, 
#             "marks" : std_marks
#         }
#         student_details.append(student)
#         print("Student added successfully!")

#     elif choice == "2":
#         print("Student Details:")
#         for i in student_details:
#             print(i["id"], i["name"], i["marks"])
            
#     elif choice == "3":
#         print("Passed Students:")
#         for i in student_details :
#             if i["marks"] >= 40 :
#                 print(i["name"],"=",  i["marks"])
    
#     elif choice == "4":
#         print("System exit successfully!")   
#         break






# student_details = []
# student_id_lists = set()
# while True:
#     print("Student Management System")
#     print("Your availabe options:")
#     print("1. Add Student\n2. View Students\n3. Passed Students\n4. Failed Students\n5. Exit")
    
#     choice = int(input("Enter your choice: "))
#     if choice == 1 :
#         std_id = input("Enter student ID :")
#         if std_id in student_id_lists:
#             print("Student ID already exists! Please use a different ID.")
#             continue
#         else:
#             student_id_lists.add(std_id)
#             std_name = input("Enter your name :")
#             std_marks = int(input("Enter student marks :"))
#             student = {
                
#                 "id" : std_id, 
#                 "name" : std_name, 
#                 "marks" : std_marks
#             }
#             student_details.append(student)
#             print("Student added successfully!")

#     elif choice == 2:
#         print("Student Details:")
#         for i in student_details:
#             print(i["id"], i["name"], i["marks"])
            
#     elif choice == 3:
#         print("Passed Students:")
#         for i in student_details :
#             if i["marks"] >= 40 :
#                 print(i["name"],"=",  i["marks"])
                
#     elif choice == 4:
#         print("Failed Students:")
#         for i in student_details :
#             if i["marks"] < 40 :
#                 print(i["name"],"=",  i["marks"])
#     elif choice == 5:
#         print("System exit successfully!")   
#         break
        
# Improve printing while displaying the list of students
# Input marks of students separately of different subjects



student_details = []
student_id_lists = set()
marks_tuples = ("Maths", "Science", "English", "Nepali", "Social_Studies")
while True:
    print("Student Management System")
    print("Your availabe options:")
    print("1. Add Student\n2. View Students\n3. Passed Students\n4. Failed Students\n5. Class Average \n6. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1 :
        std_id = input("Enter student ID :")
        if std_id in student_id_lists:
            print("Student ID already exists! Please use a different ID.")
            continue
        else:
            student_id_lists.add(std_id)
            std_name = input("Enter your name :")
            # std_marks = int(input("Enter student marks :"))
            marks = []
            for sub in marks_tuples:
                mark = int(input(f"Enter marks for {sub} : "))
                marks.append(mark)
            student = {
                
                "id" : std_id, 
                "name" : std_name, 
                "marks" : marks
            }
            student_details.append(student)
            print("Student added successfully!")
    elif choice == 2:
        print("Student Details:")
        print("ID\t Name\t Marks")
        for i in student_details:
            
            print(i["id"], "\t", i["name"], "\t", i["marks"])  # \t is used to give space between the words
            
    elif choice == 3:
        print("Passed Students:")
        print("Name")
        for i in student_details :  # Ram[56,67,89,90,56] -> 56, 67, 89,90 ,56 , Shyam[44,45,67,89,78], Hari[23,34,45,56,67]
            count = 0
            for mark in i["marks"]:
                if mark >= 40:
                    count = count + 1
            if count == 5:
                print(i["name"])
            # if i["marks"] >= 40 :
            #     print(i["name"],"=",  i["marks"])
            
                
    elif choice == 4:
        print("Failed Students:")
        print("Name")
        for i in student_details :  # Ram[,67,89,90,56] -> 56, 67, 89,90 ,56 , Shyam[44,45,67,89,78], Hari[23,34,45,56,67]
            count = 0
            for mark in i["marks"]:
                if mark >= 40:
                    count = count + 1
            if count != 5:
                print(i["name"])
    elif choice == 5:
        if not student_details :
            print("No data available")
        else:
            total_marks = 0
            total_subject = 0
            for i in student_details:
                total_marks = total_marks + sum(i["marks"]) # 56+89+90+76+51 = 362
                total_subject = total_subject + len(i["marks"]) # 5
            average = total_marks / total_subject
            print(f"Average is {average}")
            
    elif choice == 6:
        print("System exit successfully!")   
        break
        
# Improve printing while displaying the list of students
# Input marks of students separately of different subjects
# Calculate average of total students marks and display it