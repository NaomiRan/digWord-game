import random

# define variables
game_title = "word Raider"
word_list = []

# open file for loading to the list
with open("words_bank.txt") as file:
    for line in file:
        # rstrip() to remove new line character
        word_list.append(line.rstrip().lower())
# concise code: word_list=[line.rstrip() for line in file]

# select the word to guess
word_to_guess = random.choice(word_list)

# variables to track game state
misplaces_letters = []
incorrect_letters = []
max_turn = 5
cur_turn = 0
print(f"Welcome to {game_title}")
print("The length of each word is ", len(word_to_guess))
print(f"You have {max_turn - cur_turn} turns left")

# get input and validate it
while cur_turn < max_turn:
    guess = input("Your guess is ").lower()
    if len(guess) != len(word_to_guess):
        print(f"Error: Each word only contains {len(word_to_guess)} letters")
    elif (not guess.isalpha()):
        print("Error: All your guesses must be letters only.")
        continue

    # compare each letter of input with word_bank
    index = 0
    for c in guess:
        if c == word_to_guess[index]:
            print(c, end=" ")
            if c in misplaces_letters:
                misplaces_letters.remove(c)
        elif c in word_to_guess:
            if c not in misplaces_letters:
                misplaces_letters.append(c)
        else:
            if c not in incorrect_letters:
                incorrect_letters.append(c)
                print("_", end=" ")
        index += 1
    cur_turn += 1

    # check if the user wins
    if guess == word_to_guess:
        print("Congrats, you win!")
        break
    # check if the user loses
    if cur_turn == max_turn:
        print("Sorry,you lost. The word is ", word_to_guess)
        break

    print("The number of the turns you've left is ", max_turn - cur_turn)
