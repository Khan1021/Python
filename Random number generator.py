#random number guessing game

import random

number = random.randrange(1,10)
guess = int (input("Guess a number between 1 and 10: "))

while guess != number:
   if guess < number:
     print("Guess higher.Try again!")
     guess = int (input("\nGuess a number between 1 and 10: "))

else:
  print("Guess lower.Try Again!")
  guess = int (input("\nGuess a number between 1 and 10: "))


