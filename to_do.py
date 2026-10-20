data = []


while True:
    print("+++ To Do List +++\n"
          "1. Add a task\n"
          "2. View all task\n"
          "3. Remove the task\n"
          "4. Mark to be completed\n"
          "5. Exit")
    
    choice = int(input("Enter your choice :"))
    if choice in [1,2,3,4]:
        if choice == 1:
            task = input("Enter the task :").split()
            for i in task:
                data.append(i)
    
        elif choice == 2:
            print("#Tasks are#")
            for i in data:
                print(i)
            
        elif choice == 3:
            try:
                r_task = input("Enter the task to be removed :")
                data.remove(r_task)
                print(f"{r_task} removed")
            
            except Exception as e:
                print(f" exception raised {e}")
                
        elif choice == 4:
            for i,task in enumerate(data):
                print(i+1,task)
                
            completed = []
            num = int(input("Enter the task number :"))
            
            if 1 <= num <= len(data):
                completed.append((task)[num - 1])
                print("Task completed")
            else:
                print("Enter valid task number")
            
            print("completed tasks are")
            for i in completed:
                print(i)
                
    if choice == 5:
        print("thank you !")
        break