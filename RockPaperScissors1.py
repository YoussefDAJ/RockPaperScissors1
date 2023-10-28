# Rock

rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# Paper

paper_ascii = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors

scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print("Welcome to the Rock, Paper, Paper, Scissors game: ")
choice = input("Presse Enter to continue or type (Help) for the the rules").lower()
import random

if choice == "help":
    print(
        """****** RULES ******
          \n1) You choose and the computer chooses
          \n2) Rock smashes Scissors --> Rock wins
          \n3) Scissors cut Paper --> Scissors win
          \n4) Paper covers Rock --> Paper wins
          """
    )

choice = input("Enter your choice (Rock, Paper, Scissors):").lower()

if choice not in ["rock", "paper", "scissors"]:
    print(
        "Invalid choice. Please run the program again and choose rock, paper or scissors."
    )
else:
    if choice == "rock":
        print(f"\nYou chose:\n{rock_ascii}")
    elif choice == "paper":
        print(f"\nYou chose:\n{paper_ascii}")
    else:
        print(f"\nYou chose:\n{scissors_ascii}")


# Computer choice:
computer_choice = random.choice(["rock", "paper", "scissors"])

if computer_choice == "rock":
    print(f"\nComputer chose:\n{rock_ascii}")
elif computer_choice == "paper":
    print(f"\nComputer chose:\n{paper_ascii}")
else:
    print(f"\nComputer chose:\n{scissors_ascii}")


# Determine the winner:
if choice == computer_choice:
    print("It's a tie!")
elif (
    (choice == "rock" and computer_choice == "scissors")
    or (choice == "paper" and computer_choice == "rock")
    or (choice == "scissors" and computer_choice == "paper")
):
    print(f"You win! {choice} beats {computer_choice}")
else:
    print(f"You lose, {computer_choice} beats {choice}")
