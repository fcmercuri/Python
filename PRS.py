#ask user for input without showing the input (for password)
from getpass import getpass as input

print("=== Epic Battle ===")

player1 = input("Player 1, what's your choice? (R, P, S) ")
player2 = input("Player 2, what's your choice? (R, P, S) ")

if player1 == "R" and player2 == "S":
    print("Player 1 wins! as ", player1, " beats ", player2)
elif player1 == "R" and player2 == "P":
    print("Player 2 wins! as ", player2, " beats ", player1)
elif player1 == "P" and player2 == "R":
    print("Player 1 wins! as ", player1, " beats ", player2)
elif player1 == "P" and player2 == "S":
    print("Player 2 wins! as ", player2, " beats ", player1)
elif player1 == "S" and player2 == "P":
    print("Player 1 wins! as ", player1, " beats ", player2)
elif player1 == "S" and player2 == "R":
    print("Player 2 wins! as ", player2, " beats ", player1)
elif player1 == player2:
    print("It's a tie!")
else:
    print("Invalid input! Please choose R, P, or S.")





