#Hangman game 
import random
words = ["hello","family","cat","good","mothers"]
random_word = random.choice(words)
print("\n")
print("Welcome to Hangman to game....")
print("You are to guess a  letter according to the number of dashes below....")
input("Press enter to start...  ")
print("You are to guess " + str(len(random_word)) + " letter as seen in the darsh below")
for darsh in range(len(random_word)):
     print("-", end='  ')
     darsh+=1

print("\n")     
guess_letter_right = []
got_right = 0
got_wrong = 0
for letter in range(len(random_word)):
    while True:
        guess = input("Guess the letter {}:  " .format(letter+1)).lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in random_word:
                got_right+=1
            
            else:
                got_wrong+=1   
            guess_letter_right.append(guess)
            break
        
        else:
            print("Please enter only single letter")

guess_word = ''.join(guess_letter_right)  
print("These letter you imputed: ",guess_word) 
print("\tYou where to guess the word:  " ,random_word)
print("You guess " + str(got_right) + " letters correctly!")
print("You guess " + str(got_wrong) + " letters wrongly!")

  

       
        
    
        
        
        