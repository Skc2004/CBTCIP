import random

def get_num():
    while True:
        num = input("Enter a multi-digit number: ")
        if num.isdigit() and len(num) > 1:
            return num
        else:
            print("Invalid multi-digit number, enter a valid multi-digit number.")

def guess(length):
    while True:
        g = input(f"Enter your guess (must be {length} digits): ")
        if g.isdigit() and len(g) == length:
            return g
        else:
            print(f"Invalid input. Please enter a {length}-digit number.")

def hint(num, g):
    hint = ['_' for _ in range(len(num))]
    for i in range(len(num)):
        if g[i] == num[i]:
            hint[i] = g[i]
    return ''.join(hint)

def play_round(s, g):
    print(f"\n{s}'s turn to set the number.")
    number = get_num()
    attempts = 0

    print(f"\n{g}'s turn to guess the number.")
    while True:
        attempts += 1
        guess = guess(len(number))
        if guess == number:
            print(f"Correct! {g} guessed the number in {attempts} attempts.")
            return attempts
        else:
            hint = hint(number, guess)
            print(f"Hint: {hint}")

def mastermind():
    print("Who is The Mastermind!")
    pla1 = "Player 1"
    pla2 = "Player 2"
    attempts_player2 = play_round(pla1, pla2)
    attempts_player1 = play_round(pla2, pla1)
    if attempts_player1 < attempts_player2:
        print(f"\n{pla1} is crowned Mastermind!")
    else:
        print(f"\n{pla2} is crowned Mastermind!")

if __name__ == "__main__":
    mastermind()
