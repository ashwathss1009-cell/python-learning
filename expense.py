expenses = []

while True:
    print("===== EXPENSE TRACKER =====\n"

        "1. Add Expense\n"
        "2. View Expenses\n"
        "3. Total Expenses\n"
        "4. Search by Category\n"
        "5. Delete Expense\n"
        "6. Exit")

    try:
        choice = int(input("Enter your choice :"))
        if choice == 1:
            category = input('Enter the category of expense :')
            name = input("Enter the name of expense :")
            prize = int(input("Enter the amount(rs) :"))
            expense= {
                        "category":category,
                        "name":name,
                        "prize":prize
                    }
            expenses.append(expense) 
            print("Expense added successfully") 
                        
        elif choice == 2:
            print("sl","name","Price","Category")
            for i,expense in enumerate(expenses,start=1):        
                print(i,expense["name"],expense["prize"],expense["category"])
                        
        elif choice == 3:
            sump = []
            for i,expense in enumerate(expenses):
                sump.append(expense["prize"])
            print("Total sum is",sum(sump))
        
        elif choice == 4:
            u_catogery =input("Enter the catogery to find :")
            for i,expense in enumerate(expenses):    
                if expense["category"]==u_catogery:
                    print("catogery","name","prize")
                    print(expense["category"],expense["name"],expense["prize"])
                    
        elif choice == 5:
                    d_catogery =input("Enter the catogery to delete :")
                    for i,expense in enumerate(expenses):    
                        if expense["category"]==d_catogery:
                            expenses.pop(i)
                            print(expense["category"],"removed")
                        
        elif choice == 6:
            print("thanks for your experence !")
            break
        
    except Exception as e:
        print(f"Erorr acurred {e}")    
        
