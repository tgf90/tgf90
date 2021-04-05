"""
What if you wanted a game of Rock, Paper, Scissors where you have a score? And plays on a loop and
can play if Rock Paper or Scissor are capitalized or are lowercase and checks
if you input a valid response and not random characters. What if I add more to this and make this
a more complex game.

"""
import random
input("Welcome, Press Enter to Start: ")

user_score = 0
computer_score = 0
#We can have a score counter that goes up if the person wins
while True: #Has the game replay forever or if user stops
    user_choice = input("Rock, Paper, or Scissors? ").lower()
    #.lower() lets you type capitol or lower case letters
    while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        user_choice = input("Invalid, please try again: ").lower()
    #If we enter something that isn't a choice we get an error message
    random_num = random.randint(1,3)
    #choose 1,2,3 - 1 is rock 2 paper 3 scissors
    if random_num == 1:
        computer_choice = "rock"
    elif random_num == 2:
        computer_choice = "paper"
    elif random_num == 3:
        computer_choice = "scissors"

    print("Your choice:",user_choice)
    print("Computer's coice:", computer_choice)

    if user_choice == "rock":
        if computer_choice == "rock": #Can use an AND statement
            print("It's a tie!")
        elif computer_choice == "paper":
            print("You lost!")
            computer_score += 1
            #score goes up by 1
        elif computer_choice == "scissors":
            print("You win!")
            user_score += 1
    if user_choice == "paper":
        if computer_choice == "paper":
            print("It's a tie!")
        elif computer_choice == "rock":
            print("You win!")
            user_score += 1
        elif computer_choice == "scissors":
            print("You lost!")
            computer_score += 1
    if user_choice == "scissors":
        if computer_choice == "scissors":
            print("it's a tie!")
        elif computer_choice == "rock":
            print("You lose!")
            computer_score += 1
        elif computer_choice == "paper":
            print("You win!")
            user_score += 1

    print("Your score")
    print(user_score)
    print("Computer score")
    print(computer_score)
    repeat = input("Play Again? (Y/N) ").lower()
    while repeat != "n" and repeat != "y":
        repeat = input("Invalid input, please try again: ").lower()

    if repeat == "n":
        break
    #Asks the user if they want to play again?