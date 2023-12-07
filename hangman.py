import random
from re import A
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  #randomly chooses something from the list
    while '_' in word or ' ' in word:
        word = random.choice(words)
       
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase) 
    used_letters = set()  # what the user has guessed


    lives=6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have' , lives, 'lives left and You have used these letters: ',' '.join(used_letters))

        # what the current word is
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1 # takes away a life if wrong
                print('Letter is not in the word.')


        elif user_letter in used_letters:
            print('You have already used that characte, please try again.')


        else:
            print('Invalid character.Please try again.')

# gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0: 
        print(f'You ran out of lives. The word was  ' )
        print('You died, sorry.The word was', word)
      
        print('__')
        print('|   |')
        print('|   o')
        print('|  \|/')
        print('|  / \ ')
        print('|__')
    
    else:
        print('You guessed the word', word, '!!')



# function needs to be called 
hangman()


