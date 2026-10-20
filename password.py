import random
import string

character = string.ascii_letters + string.digits + string.punctuation

while True :
    print("## Password generator ##\n"
          "1. Generate password\n"
          "2. Multiple password \n"
          "3. Exit ")
    choice = int(input("Enter your choice :"))
    
    if choice ==1:
        password = ""
        length = int(input("Enter the length of password :"))
        for i in range(length):
            password += random.choice(character)
        print("password is ",password)
        
    elif choice == 2:
        m_password = []
        
        m_length = int(input("Enter the length of password :"))
        number = int(input("Enter the number of password :"))
        for x in range(number):
            word = ""
            for i in range(m_length):
                word += random.choice(character)
            m_password.append(word)
            
        print("multiple passwords are ")
        for i in m_password:
            print(i)
        
    elif choice == 3:
        print("good bye !")
        break
        
        
        
        
        
        
        
        