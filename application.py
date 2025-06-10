import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number (1-100). Type 'exit' to quit.")

    while True:
        guess = input("Your guess: ").strip()
        if guess.lower() == 'exit':
            print(f"Game over. The number was {number}.")
            break
        # Intentional flaw: does not check for negative numbers or numbers > 100
        if not guess.isdigit():
            print("Invalid input. Enter a number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! Attempts: {attempts}")
            break

if __name__ == "__main__":
    play_game()