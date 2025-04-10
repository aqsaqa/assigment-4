import random 

# Function to choose a random word
def get_random_word():
    words = ['python', 'hangman', 'computer', 'programming', 'developer', 'language']
    return random.choice(words)

# Function to display the current status of the game
def display(word, guessed_letters):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display_word

# Function to check if the user has guessed the word correctly
def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def hangman():
    print("Welcome to Hangman Game!")
    word = get_random_word()  # Select a random word
    guessed_letters = []  # List to store the guessed letters
    attempts_left = 6  # Number of attempts before losing

    print("The word has", len(word), "letters.")
    
    # Main game loop
    while attempts_left > 0:
        print("\nWord to guess:", display(word, guessed_letters))
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", attempts_left)
        
        # User input for guess
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter at a time.")
            continue

        # If letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guessed letter to guessed_letters
        guessed_letters.append(guess)

        # If guess is incorrect, reduce attempts
        if guess not in word:
            attempts_left -= 1
            print(f"Wrong guess! The letter {guess} is not in the word.")
        
        # Check if the user has won
        if check_win(word, guessed_letters):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
        
    if attempts_left == 0:
        print("\nGame Over! You've run out of attempts. The word was:", word)

hangman()
