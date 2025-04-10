import random

def number_guess_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess it? Let's play!\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please guess a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("📉 Too low! Try again.\n")
            elif guess > secret_number:
                print("📈 Too high! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")

number_guess_game()
