import random
def play_game():
    choices=["rock", "paper", "scissors"]
   


    while True:
       
        user_choice=input("enter your choicse (rock/paper/scissors): ").lower()
        
        if user_choice == "quit":
            print("Game stopped. Bye!")
            break

        if user_choice not in choices:
            print("Invalid choice, try again!")
            continue

       
        computer_choices=random.choice(choices)
        if user_choice==computer_choices:
            print(f' the answer is {computer_choices}, we are  Draw !')
            break

        elif(
            (user_choice == "rock" and computer_choices == "scissors") or
            (user_choice == "paper" and computer_choices== "rock") or
            (user_choice == "scissors" and computer_choices == "paper")
        ):
           print(f"Computer chose {computer_choices}, you win!")  


        else: 
            print(f' the computer_choices is {computer_choices}, you lose')


play_game() 


























    
