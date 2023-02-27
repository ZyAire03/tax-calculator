import random

# rock, paper scissors

# computer_choice = 'scissors'
computer_choice = random.choice(['scissors', 'paper', 'rock'])

user_choice = input('Do you want: rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print('TIE')

elif user_choice =='rock' and computer_choice == 'scissors':
    print( 'You Won!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You Won!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You Won')
else:
    print('You Lose: Computer wins :D')
