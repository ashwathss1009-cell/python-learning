data = {}

while True:
    print("### Student Managment System ### \n" 
    "\n"
    "1. Add Student\n"
    "2. Display All Students\n"
    "3. Search Student\n"
    "4. Add Course\n"
    "5. Remove Course\n"
    "6. Add Skill\n"
    "7. Display All Unique Skills\n"
    "8. Show Students Enrolled in a Course\n"
    "9. Delete Student\n"
    "10. Exit\n"
    "\n")
    choice = int(input("Enter your choice:  "))
    
    if choice in [1,2,3,4,5,6,7,8,9]:
        if choice ==1:
            roll = int(input("Enter the roll_number of the student:     "))
            data[roll] = {}
            data[roll]["personal"] = []
            name = input("Enter the name of student:    ")
            age  = int(input("Enter the age of student:    "))
            data[roll]["personal"].append(name)
            data[roll]["personal"].append(age)
            
            data[roll]["course"] = []
        
            sub = input("enter the course took by the student:  ").split()
            for i in sub:
                data[roll]["course"].append(i)
                
            data[roll]["skill"] = set()
            
            s = input("Enter the skill that student has:    ").split()
            for i in s:
                data[roll]["skill"].add(i)
                
        elif choice == 2:
            try:
                for key,value in data.items():
                    v_name ,v_age = value["personal"]
                    print(f" ID -{key} \n"
                          f" Name - {v_name} \n"
                          f" Age - {v_age}\n"
                          f" Course - {",".join(value["course"])}\n"
                          f" Skill - {",".join(value["skill"])}\n")
                    
                    
            except Exception as e:
                print(e,"raised an exception")
                
            except:
                print("students data not entered")
                
        elif choice == 3:
            s_roll = int(input("Enter the student roll_number to be searched:  "))
            print(data[s_roll])  
        
        elif choice == 4:
            add_course = input("Enter the new course to be ").split()
            roll = int(input("Enter the roll_number of student whose course to be modified "))
            for i in add_course:
                data[roll]["course"].append(i)
            print("Course added successfully !")
            for value in data.values():
                print("the updated courses are",",".join(value["course"]))
                
                
        elif choice == 5:
            remove_course = input("Enter the course to be removed ").split()
            roll = int(input("Enter the roll_number of student whose course to be remove "))
            for i in remove_course:
                data[roll]["course"].remove(i)
            print("Course deleated successfully !")
            for value in data.values():
                print("the updated courses are",",".join(value["course"]))   
                
        elif choice == 6:
            roll = int(input("Enter the roll_number of the student whose need to update skill:  "))
            new_skill = input("Enter the new skill ").split()
            for i in new_skill:
                data[roll]["skill"].add(i)
            print("skills added succesfully")
            for value in data.values():
                print("the updated courses are",",".join(value["skill"]))
                
        elif choice == 7:
            for key,value in data.items():
                v_name ,v_age = value["personal"]
                print(f"{v_name} skill are {",".join(value["skill"])}")
                
        elif choice == 8:
            c_name = input("Enter the course:   ")
            found = False
            
            for key,value in data.items():
                if c_name in value["course"]:
                    name = value["personal"][0]
                    roll = value["personal"][1]
                    print(f" ID - {roll} ,name {name}")
                    found = True
                    
            if not found:
                print(f"no students has enrolled this course")
                            
        elif choice == 9:
            roll = int(input("Enter the student roll_number who want to delete: "))
            data.pop(roll,"not found")
            print(f"removed successully")
            
            
    if  choice == 10:
        print("thank you !")
        break
            
    if choice not in [1,2,3,4,5,6,7,8,9,10]:
        print("Please Enter the choice correctly")
            