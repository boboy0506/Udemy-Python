import random

from words import word_list
from art import logo
from art import stages

# picks a random word inside a words.py
chosen_word = random.choice(word_list)

# get the total length of a word 
word_length = len(chosen_word)

# declares the lives and boolean value of the game
end_of_game = False
lives = 6

print(logo)

# converts the picked word into _
display = []
for _ in range(word_length):
    display += "_"

# loops the entire game, if the lives reached 0 the game will end or if you completed the word you win
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    # checks if you already entered what you entered last time
    if guess in display:
        print(f"You've already guessed {guess}")
        
    # checked the guess letter
    for positon in range(word_length):
        letter = chosen_word[positon]
        # replaces the _ with the correct letter
        if letter == guess:
            display[positon] = letter
    
    # check if the user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life")
        lives-= 1
        if( lives == 0):
            end_of_game = True
            print("You lose")
    # pirnts the words 
    print(f"{' '.join(display)}")
        
    if "_" not in display:
        print("You win")
        end_of_game = True
        
    print(stages[lives])