import random as r

rNum = r.randint(1, 100)
yTries = 0
def game(number, tries):
    guess = int(input("Guess the number between 1 and 100: "))
    if(guess<number):
        tries += 1
        print("Too low, try again!")
        return True
    if(guess>number):
        tries += 1
        print("Too high, try again!")
        return True
    if(guess == number):
        tries += 1
        print(f"You won in {tries}, congratulations!")
        return False
while(game(rNum, yTries)):
    yTries += 1

