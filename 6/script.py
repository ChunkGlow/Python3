import random

def random_guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    print("Welcome to the Random Guessing Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    random_guessing_game()
