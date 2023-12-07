# Quiz


print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great,let's play! :)")
score = 0

answer = input("When is Zaynab's birthday? ")
if answer == "21/10":
    print("Correct! Well done, next question.")
    score += 1

else:
    print("incorrect!")



answer = input("What colour is her cat? ").lower()
if answer == "grey":
    print("Correct! Well done, next question.")
    score += 1
else:
    print("incorrect!")

answer = input("Final question.....what is one of her interests? ").lower()
if answer == "videogames":
    print("Correct!.")
    score += 1
else:
    print("incorrect!")



print("You got " + str(score) + " questions correct!")
print("You got " + str((score/3) * 100) + "%.")




