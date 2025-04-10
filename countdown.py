import time 

def countdown_timer(seconds):
    while seconds > 0:
        # Calculating minutes and seconds from the total seconds
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02}:{secs:02}'  # Formatting time in mm:ss format
        print(timeformat, end='\r')  # Prints the time, overwrites the line with each update
        time.sleep(1)  # Waits for 1 second before updating the time
        seconds -= 1  # Decreases the countdown by 1 second

    print("00:00")  # Once the timer reaches 0, display 00:00
    print("Time's up!")  # Notify user that time is up

# Main function to start the timer
def main():
    print("Welcome to the Countdown Timer!")
    try:
        # User input to enter the time in seconds
        total_seconds = int(input("Enter the time in seconds: "))
        countdown_timer(total_seconds)  # Start the countdown
    except ValueError:
        print("Please enter a valid number for seconds.")  # Error handling for non-integer input

# Run the program
main()
