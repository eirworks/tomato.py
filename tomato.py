# function that take a parameter number and text
# every 1 seconds it display the text and reduce number by 1 until number is 0
# then it display "Time is up" and stop
import time, sys, os

def tomato(number, text):
    
    while number > 0:
        # catch keyboard interrupt display "Time is up" and stop
        try:
            # variable to store timedelta of number in seconds
            time_delta = time.gmtime(number)
            print(text, time_delta.tm_min, ":", time_delta.tm_sec, end="\r")
            time.sleep(1)
            number -= 1
        except KeyboardInterrupt:
            print("Quitting task")
            break

    print("Time is up")
    # call system command "notify-send" to display a notification with text "Time is up"
    os.system("notify-send 'Time is up'")


# function pomodoro that run tomato function with 25 minutes and text from parameter
def pomodoro(text):
    tomato(25*60, text)

# function pomodoro_break that run tomato function with paramters: minutes (default 5) and text
def pomodoro_break(text, minutes=5):
    tomato(minutes*60, text)

# run pomodoro function with parameter text from command line arguments if first argument is "pomodoro"
# else if first argument is "break" run short_break function with parameter text from command line arguments
if sys.argv[1] == "task":
    pomodoro(sys.argv[2])
elif sys.argv[1] == "break":
    pomodoro_break("Short break")
elif sys.argv[1] == "long":
    pomodoro_break("Long break", 15)
else:
    print("Invalid command")