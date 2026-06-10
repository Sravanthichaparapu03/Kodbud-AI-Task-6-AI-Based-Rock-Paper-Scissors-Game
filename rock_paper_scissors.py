import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("Rock Paper Scissors Game")
print("Type 'exit' to quit")

while True:
    user = input("\nChoose Rock, Paper, or Scissors: ").lower()

    if user == "exit":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("Result: Tie")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("Score -> You:", user_score,
          "| Computer:", computer_score)
