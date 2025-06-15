import random

options = {"s": 1, "w": -1, "g": 0}
names = {1: "Snake", -1: "Water", 0: "Gun"}

rules = {
    (1, -1): "win",
    (1, 0): "lose",
    (-1, 1): "lose",
    (-1, 0): "win",
    (0, 1): "win",
    (0, -1): "lose",
}

try:
    rounds = int(input("How many rounds? "))
except:
    print("Enter a number next time.")
    exit()

p_score = 0
c_score = 0

for i in range(rounds):
    print(f"\nRound {i + 1}")
    pick = input("Pick s (Snake), w (Water), or g (Gun): ").lower()

    if pick not in options:
        print("Invalid input.")
        continue

    player = options[pick]
    comp = random.choice(list(options.values()))

    print(f"You: {names[player]}")
    print(f"Computer: {names[comp]}")

    if player == comp:
        print("Draw.")
    else:
        outcome = rules.get((player, comp), "lose")
        if outcome == "win":
            print("You win this round.")
            p_score += 1
        else:
            print("You lose this round.")
            c_score += 1

print("\nFinal Result:")
print(f"You: {p_score} | Computer: {c_score}")

if p_score > c_score:
    print("You won the game!")
elif p_score < c_score:
    print("Computer won the game!")
else:
    print("It's a tie!")