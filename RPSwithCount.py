# Rock-Paper-Scissors game with score tracking for two players

score1 = 0
score2 = 0

while True:
    # Validate Player 1 input
    player1 = input("Player 1, what's your choice? (R=Rock, P=Paper, S=Scissors): ")
    if player1 not in ("R", "P", "S"):
        print("Invalid input for Player 1! Please choose R, P, or S.")
        continue

    # Validate Player 2 input
    player2 = input("Player 2, what's your choice? (R=Rock, P=Paper, S=Scissors): ")
    if player2 not in ("R", "P", "S"):
        print("Invalid input for Player 2! Please choose R, P, or S.")
        continue

    if player1 == "R" and player2 == "S":
        print("Player 1 wins! as ", player1, " beats ", player2)
        score1 += 1
    elif player1 == "R" and player2 == "P":
        print("Player 2 wins! as ", player2, " beats ", player1)
        score2 += 1
    elif player1 == "P" and player2 == "R":
        print("Player 1 wins! as ", player1, " beats ", player2)
        score1 += 1
    elif player1 == "P" and player2 == "S":
        print("Player 2 wins! as ", player2, " beats ", player1)
        score2 += 1
    elif player1 == "S" and player2 == "P":
        print("Player 1 wins! as ", player1, " beats ", player2)
        score1 += 1
    if score1 > 3:
        print("Player 1 is the overall winner!, with score of ", score1, "vs ", score2)
        exit()
    elif score2 > 3:
        print("Player 2 is the overall winner!, with score of ", score2, "vs ", score1)
        exit()
    print("Score: Player 1 =", score1, ", Player 2 =", score2)

    if score1 >= 3:
        print("Player 1 is the overall winner!, with score of ", score1, "vs ", score2)
        exit()
    elif score2 >= 3:
        print("Player 2 is the overall winner!, with score of ", score2, "vs ", score1)
        exit()

print("Game over")