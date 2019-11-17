import random
# Write your code here
tries = 0
words = ["python", "java", "kotlin", "javascript"]
key = random.choice(words)
guessed = []
all_guessed = []
show = list("-" * len(key))
print(" ".join("HANGMAN"))


def ask_to_play():
    global tries
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == "play" or choice == "exit":
        if choice == "play":
            tries = 8
            play()
        elif choice == "exit":
            tries = 0
    else:
        tries = 0


def play():
    global tries
    global key
    global guessed
    global all_guessed
    global show
    key = random.choice(words)
    guessed = []
    all_guessed = []
    show = list("-" * len(key))
    while tries > 0:
        print()
        print("".join(show))
        guess = input("Input a letter: ")
        if len(list(guess)) > 1 or len(list(guess)) < 1:
            print("You should print a single letter")
        elif not guess.islower() or guess.isupper():
            print("It is not an ASCII lowercase letter")
        elif guess in all_guessed:
            print("You already typed this letter")
        else:
            if guess in key:
                show = []
                if guess not in guessed:
                    guessed.append(guess)
                for x in key:
                    if x not in guessed:
                        show.append("-")
                    else:
                        show.append(x)
            else:
                tries -= 1
                print("No such letter in the word")
        all_guessed.append(guess)
        if "-" not in show:
            print("You guessed the word! \nYou survived!")
            ask_to_play()
            break
    if "-" in show:
        print("You are hanged!")
        ask_to_play()


ask_to_play()
