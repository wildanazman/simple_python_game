import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]
computer_choice = random.choice(game)


user = int(input("choose 0 for rock, 1 for paper, 2 for scissors "))
user_choice = game[user]
print(f"computer choose {computer_choice}")
print(f"user choose {user_choice}")


if user_choice == rock and computer_choice == scissors:
    print("you won!")
elif user_choice == rock and computer_choice == paper:
    print("you lose.")
elif user_choice == scissors and computer_choice == rock :
    print("you lose.")
elif user_choice == scissors and computer_choice == paper:
    print("you won.")
elif user_choice == paper and computer_choice == rock:
    print("you won.")
elif user_choice == paper and computer_choice == scissors:
    print("you lost.")
elif user_choice == computer_choice:
    print("it's a draw!")
