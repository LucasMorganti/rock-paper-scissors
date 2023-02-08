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

#Write your code below this line 👇
options = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
ai = random.randint(0, 3)

print(f"Player pick:\n{options[player]}")
print(f"Ai pick:\n{options[ai]}")

if player == ai:
  print("It's a draw!")
elif player == 0 and ai == 1:
  print("Player lost!")
elif player == 0 and ai == 2:
  print("Player won!")
elif player == 1 and ai == 0:
  print("Player won!")
elif player == 1 and ai == 2:
  print("Player lost!")
elif player == 2 and ai == 0:
  print("Player lost!")
elif player == 2 and ai == 1:
  print("Player won!")
