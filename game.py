import random

def guess_the_number_game():
    print("Welcome to the 'Guess the Number' game!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(lower_bound, upper_bound)
    
    # Initialize number of attempts
    attempts = 0
    
    print(f"Guess the number between {lower_bound} and {upper_bound}:")
    
    while True:
        # Ask the user for their guess
        guess = int(input("Enter your guess: "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts!")
            break


guess_the_number_game()
