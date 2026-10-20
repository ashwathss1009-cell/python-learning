def sum(a,b,c=0):
    return a+b+c

def subract(a,b,c=0):
    return a-b-c

def multiply(a,b,c=1):
    return a*b*c

def division(a,b):
    return a/b

while True:
    print("\n### Calculator ###\n"
        "1. Addition\n"
        "2. Subraction\n"
        "3. Multiply\n"
        "4. Division\n"
        "5. Exit")
        
    choice = int(input("Enter your choice   :"))
    a = int(input("Enter your first number :"))
    b = int(input("Enter your second number ;"))
    c = int(input("Enter your third number :"))
    if choice in [1,2,3,4]:
        
        if choice  == 1:
            print("The sum is ",sum(a,b,c))
        
        if choice == 2:
            print("the subraction is",subract(a,b,c))
            
        if choice == 3:        
            print(f"the multiplication is {multiply(a,b,c)}")
        
        if choice == 4:
            a = int(input("Enter your divident number :"))
            b = int(input("Enter your divider number :"))
            print(f"The division is {division(a,b)}")
            
                        
    if choice == 5:
        print("Thank you !")
        break