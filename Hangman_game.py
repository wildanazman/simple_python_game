import random

from unicodedata import category

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
fruit = ["pineapple","banana", "apple", "orange","pear","watermelon"]
vegetable = ["tomato","cucumber", "brocolli", "spinach","lettuce"]

word_list = random.choice([fruit,vegetable])
category = "Fruits" if word_list == fruit else "Vegetables"
print(f" the category for today is {category}")

lives = 6
chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
words_count=(len(placeholder))
print(f"there are {words_count} letter. Fill in the blank. You have 6 chances only.")
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)


    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True
            print("game over")


    print(stages[lives])
    print(display)
    print(f"you only have {lives} left.")
    if "_" not in display:
        game_over = True
        print(f"The answer is {display}. You win.")
