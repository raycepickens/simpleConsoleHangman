import requests
import os
import time
'''
Hangman functionality
'''

def hangman_functionality(api):
    word=api[0]
    word = word.strip("[]'").lower()
    length = len(word)
    print(word)
    print("your word is ", length , " characters long....\nHappy Guessing!!!!")
    
    time.sleep(3)
    clear_console()
    wordArray=[]
    playerView=[]
    for i in range (length):
        wordArray.append(word[i])
        playerView.append("*")
    
    

    
    i=0
    while(i < 7):
        print("Guess a letter or guess the whole word!")
        print("1. Guess a letter\n2.Guess the word")
        guess= input()
        if (guess =="1"):
            print("guess a letter")
            letterGuess=input().lower()
            i+=1
            clear_console()
            check_for_letter(wordArray,playerView,letterGuess)
            if "*" not in playerView:
                print("you win!!!")
                time.sleep(4)
                break
            if ( i == 7):
                print("Sorry you lose...")
                time.sleep(4)
        elif (guess == "2"):
            
            print("guess a word")
            wordGuess=input().lower()
            if (wordGuess == word):
                print("You win!!!!!")
                time.sleep(4)
                break
            else:
                print("Nope not it, loser")
                i+=1
                if ( i == 7):
                    print("Sorry you lose...")
                    time.sleep(4)

        else:
            print("enter a valid answer please")
            
            time.sleep(2)
            clear_console()
    

  






def check_for_letter ( wordArray, playerView, letterGuess):
    found = False
    for i, letter in enumerate(wordArray):
        if letter == letterGuess:
            playerView[i] = letterGuess
            found = True
    if found:
        print(playerView)
    else:
        print("Nope, not in there")



    


def api_call(mode):
    if (mode =="1"):
        endpoint=4
    if (mode =="2"):
        endpoint=5
    if (mode =="3"):
        endpoint=6
    
    url="https://random-word-api.herokuapp.com/word?length="+str(endpoint)
    response= requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
