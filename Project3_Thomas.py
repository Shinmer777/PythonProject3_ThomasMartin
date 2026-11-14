import random
words = ["apple", "house", "python", "planet", "guitar"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
def display_word():
    displayed = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed = displayed + letter + " "
        else:
            displayed = displayed + "_ "
    print("Secret word:")
    print(displayed)
def check_game_status(current_incorrect):
    won = True
    for letter in secret_word:
        if letter not in guessed_letters:
            won = False
    if won:
        print("\nCongratulations! You guessed the word!")
        print("Final word:")
        display_word()
        return "won"
    if current_incorrect >= max_guesses:
        print("\nGame over! You ran out of attempts.")
        print("The secret word was:", secret_word)
        return "lost"
    return "continue"
def play_game():
    current_incorrect = incorrect_guesses
    game_over = False
    while not game_over:
        print()
        display_word()
        print("Guessed letters:", guessed_letters)
        print("Incorrect guesses remaining:", max_guesses - current_incorrect)
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or guess < "a" or guess > "z":
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one!")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            current_incorrect = current_incorrect + 1
        status = check_game_status(current_incorrect)
        if status == "won" or status == "lost":
            game_over = True
if __name__ == "__main__":
    play_game()