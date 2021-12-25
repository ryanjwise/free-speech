import os

def get_input():
    user_input = input("What would you like to say?")
    return user_input

def play_input(input):
    os.system(f"espeak '{input}'")

def app_loop():
    loop = True
    while loop:
        user_input = get_input()
        play_input(user_input)
        os.system('clear')
        if user_input == "exit":
            loop = False
            print("Goodbye")

app_loop()