#This is a guessing game

import random
number = random.randint(1,30)

print("what is your name?")
name = input()
print("Alright " + name + " this is a guessing game and you are to guess the number that i have thought of between 1-30")

guessestaken = 0

while guessestaken < 4:
    print("Take a guess " +   name )
    guess = input()
    guess = int(guess)
    guessestaken = guessestaken + 1

    if guess > number:
        print("Nahh, too big")
    
    if guess < number:
        print("Too small, just like your brain")

    if guess == number:
        break
 
if guess == number:
    guessestaken = str(guessestaken)
    print("Brilliant!, this is correct " + name + " , you've guessed correctly")

if guess != number:
    number = str(number)
    print("You've lost the game, try again NEVER!!!, also the number i was thinking of is " + number)




