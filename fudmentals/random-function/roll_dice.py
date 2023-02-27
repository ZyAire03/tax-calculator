import random
roll = random.randint(1,6)
# returns a random number 1-6
# print('The cumputer rolled a '+ str(roll))

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print('Incorrect! They rolled a ' + str(roll))

