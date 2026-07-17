import random
print("Welcome to Hangman!")
words=["python",
       "computer",
       "apple",
       "coding",
       "student"]

secret_word=random.choice(words)
print("The word has",len(secret_word),"letters.")
guessed_letters = []
lives = 6
while lives > 0:

    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    if all(letter in guessed_letters for letter in secret_word):
        print("You win! The word was:", secret_word)
        break

    guess = input("Guess a letter: ")
    if len(guess) != 1 or not guess.isalpha():
     print("Please enter a single letter.")
     continue
    if guess in guessed_letters:
        print("You already guessed that letter. Try a new one.")
        continue

    if guess in secret_word:
        print("correct guess")
    else:
        print("wrong guess")
        lives = lives - 1



    guessed_letters.append(guess)

    print("guessed_letters:", guessed_letters)
    print("Lives left:", lives)

if lives == 0:
    print("You lost! The word was:", secret_word)


