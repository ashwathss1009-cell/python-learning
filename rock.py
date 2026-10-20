import random
choices = ["rock","paper","scissors"]
u_score = 0
c_score = 0
draw = 0

while True:
    print("=== Rock Paper Scissors ===\n"
        "1. Play game\n"
        "2. View Score\n"
        "3. Exit\n")
    
    choice = int(input("Enter your choice :"))
    computer = random.choice(choices)

    if choice == 1:
        print("#pick one#\n"
              "Rock 🪨\n"
              "Paper 📄\n"
              "Scissors ✂️\n")
        
        user = input("Enter your pick :")
        if user == computer :
            print("Draw")
            draw +=1
        elif user == "rock" and computer == "scissors":
            print("user")
            u_score +=1
        elif user == "scissors" and computer == "rock":
            print("computer")
            c_score +=1
        elif user == "paper" and computer == "rock":
            print("user")
            u_score +=1
        elif user == "rock" and computer == "paper":
            print("computer")
            c_score +=1
        elif user == "paper" and computer == "scissors":
            print("computer")
            c_score +=1
        elif user == "scissors" and computer == "paper":
            print("user")
            u_score +=1
            
    if choice == 2:
        if u_score > c_score and u_score>draw :
            print(f"User is winner ! with {u_score} points")
            print(f"computer - {c_score}")
        elif c_score > u_score and c_score >draw:
            print(f"computer is winner ! with {c_score} points")
            print(f"user - {u_score}")
        elif c_score == u_score:
            print(f"draw")
            print(f"user - {u_score} \nComputer - {c_score}")
    
    if choice == 3:
        print("thanks for playing")
        break
        