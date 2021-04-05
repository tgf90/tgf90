#Guessing Game

print("Welcome to the Guessing Game!")

answer = "5"
guess = input("Provide a number: ")
while guess != answer:
    print("Your response, " + guess + " , was incorrect.")
    guess = input("Provide a new number: ")
print("You did it!")