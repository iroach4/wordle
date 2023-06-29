import random

f = open("wordle_words.txt", "r")
data = f.readlines()
f.close()

wordle_words = []
for word in data:
    wordle_words.append(word[0:5])

def format_word(word):
    for letter in word:
        print(letter, end = "   ")
    print(" ")

def format_guess(word):
    for letter in word:
        print(letter, end = "       ")
    print(" ")

def create_board():
    for item in board:
        for underscore in item:
            print(underscore, end = " ")
        print("\n")

def play_wordle():
    answer = random.choice(wordle_words)

    board = [["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"]]

    for idx in range(6):
        guess = input("Guess: ") #make sure its all letters and only 5 characters long
        while len(guess) != 5 or guess.isalpha() == False:
            print("Invalid guess, guess must be 5 letters, try again.")
            guess = input("Guess: ")


        underline = ["_", "_", "_", "_", "_"]

        for index in range(len(guess)):
            letter = guess[index]
            board[idx][index] = letter
            if letter in answer and answer[index] != letter:
                underline[index] = "Yellow"
            elif letter in answer and answer[index] == letter:
                underline[index] = "Green"
            else:
                underline[index] = "Grey"

        format_guess(guess)
        format_word(underline)

        count = 0
        for item in underline:
            if item == "Green":
                count += 1
        if count == 5:
            print(" ")
            print("YOU WIN! \n" * 5)
            break

        if idx == 5:
            print(" ")
            print("YOU LOSE! \n" * 5)
            print(" ")
            print("The answer was " + answer)
        
        print(" ")

play_wordle()

play_again = input("Would you like to play again? 1 for Yes, 0 for No: ")
while play_again == "1":
    play_wordle()
    play_again = input("Would you like to play again? 1 for Yes, 0 for No: ")

