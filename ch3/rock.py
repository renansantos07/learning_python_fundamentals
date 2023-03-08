import random

# random_choice = random.choice(['rock', 'paper', 'scissors']) <--
# Está é uma forma mais simples de fazer o que está sendo executado a baixo,
# usamos menos linhas e não seria necessario utilizar o IF

winner = ''
random_choice = random.randint(0, 1)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

user_choice = ''

while (user_choice != 'rock' and
       user_choice != 'paper' and
       user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')

if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'computer'
else:
    winner = 'user'

if winner == 'Tie':
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner, 'won. The Computer chose', computer_choice + '.')
