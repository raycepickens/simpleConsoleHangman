import time
import os
from hangman import hangman_functionality, api_call
'''
#Hangman Project
#Creation Date: 4/5/24
#Last Edit# 4/6/24
#Creator: Rayce Pickens
'''
def main():
    print("##########\nWelcome To Hangman!\n#########")

    time.sleep(2)
    clear_console()

    while(True):

        print("What would you like to do?")
        print("1: Play Easy Mode?")
        print("2: Play Intermediate Mode?")
        print("3: Play Hard Mode?")
        print("4. Quit?")
        answer =input()
        
        clear_console()
        print("Loading")
        time.sleep(1)
        clear_console()
        print("Loading.")
        time.sleep(1)
        clear_console()
        print("Loading..")
        time.sleep(1)
        clear_console()
        print("Loading...")
        time.sleep(1)
        clear_console()
        


        if (answer =="4"):
            print("Goodbye!")
            break
        
        elif answer == "1" or answer == "2" or answer == "3":
            hangman_functionality(api_call(answer))


        else:
            print("enter a valid answer please")
            time.sleep(2)
            clear_console()
    



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()