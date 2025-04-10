import random 

def get_computer_choice():
    # Computer ke liye ek random choice banaiye
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    # User se input lete hain
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose from rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    #  user aur computer ke choices ko compare karte hain
    if user_choice == computer_choice:
        return "It's a tie!"
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    
    else:
        return "Computer wins!"

def play_game():
    # Game ki main function jo sab kuch control karega
    print("Rock, Paper, Scissors Game!")
    
    user_choice = get_user_choice()  # User ka choice lete hain
    computer_choice = get_computer_choice()  # Computer ka random choice
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)  # Winner ka result determine karte hain
    print(result)

play_game()
