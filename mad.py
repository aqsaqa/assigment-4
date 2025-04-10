def mad_libs_game():
    print("Welcome to Mad Libs Game!")

    # Asking for user input
    noun1 = input("Enter a noun (e.g., dog, car, tree): ")
    verb1 = input("Enter a verb (e.g., run, jump, swim): ")
    adjective1 = input("Enter an adjective (e.g., happy, funny, large): ")
    noun2 = input("Enter another noun (e.g., chair, apple, school): ")
    verb2 = input("Enter another verb (e.g., eat, play, write): ")
    adjective2 = input("Enter another adjective (e.g., tall, soft, shiny): ")

    # Creating the story
    story = f"Once upon a time, a {adjective1} {noun1} decided to {verb1}. It saw a {adjective2} {noun2} and wanted to {verb2} with it. " \
            f"The {noun1} and the {noun2} became the best of friends and lived happily ever after."

    # Printing the story
    print("\nHere is your Mad Libs story:")
    print(story)

mad_libs_game()
