import random

randNum = random.randint(1, 100)
# print(randNum)

userGuess = None
guesses = 0

print("Guess a number between 1 and 100\n")

while userGuess != randNum:
    try :
        userGuess = int(input("Enter your Guess: "))
    except :
        print("Invalid input, Please enter Integer Values only.")
        continue
    guesses += 1
    if userGuess == randNum:
        print("You guesses it right!")
    elif userGuess < randNum:
        print("You guesses it wrong! Please try a greater number.\n")
    else:
        print("You guesses it wrong! Please try a smaller number.\n")

print(f"Great! You guessed it right in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if hiscore > guesses:
    print("Congrats! You have broken the highest score.")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
