print("Rock, Paper, Scissors Game")

# Get choices from both players
user = input("Player 1 - Enter rock, paper, or scissors: ").lower()
computer = input("Player 2 - Enter rock, paper, or scissors: ").lower()

print("Player 1 chose:", user)
print("Player 2 chose:", computer)

# Decide the winner
if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("Player 1 wins!")
elif user in ["rock", "paper", "scissors"] and computer in ["rock", "paper", "scissors"]:
    print("Player 2 wins!")
else:
    print("Invalid input by one or both players!")
