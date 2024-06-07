import random
wins = 0
losses = 0
ties = 0
options = ['rock', 'paper', 'scissors']
# Create a loop that will ask the player to select wether to keep playing or exit the loop and finish the application
# If the player chooses to keep playing, the game will start again
# If the player chooses to exit the loop, the application will finish
while True:
    # Let the player choose between rock, paper and scissors and save their input in lowercase in a variable
    print('Choose between rock, paper and scissors')
    playerSelection = input().lower()
    # Validate player's input against options
    while playerSelection not in options:
        print('Invalid option, please choose between rock, paper and scissors')
        playerSelection = input().lower()
    # choose a random option between rock paper and scissors for the computer
    computerSelection = random.choice(options)
    # Print the computer's selection
    print('The computer selected: ' + computerSelection)
    # Print wether the user has won against the computer
    if playerSelection == 'rock' and computerSelection == 'scissors':
        print('You win!')
        wins += 1
    elif playerSelection == 'paper' and computerSelection == 'rock':
        print('You win!')
        wins += 1
    elif playerSelection == 'scissors' and computerSelection == 'paper':
        print('You win!')
        wins += 1
    elif playerSelection == computerSelection:
        print('It is a tie!')
        ties += 1
    else:
        print('You lose!')
        losses += 1
    
    print('Do you want to play again?')
    print('Yes')
    print('No')
    option = input()
    if option == 'No':
        break
# Print the number of wins, losses and ties
print('Wins: ' + str(wins))
print('Losses: ' + str(losses))
print('Ties: ' + str(ties))
# Print a message to say goodbye to the player
print('Goodbye!')