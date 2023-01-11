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

print("Welcome to the Rock-Papers-Scissors game!\n")

player_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

option_list = [rock, paper, scissors]

if player_option >= 3 or player_option < 0:
  print("You typed an invalid number. Try again!")
else:
  print(f"You chose: {option_list[player_option]}") #prints index from option_list variable above


  computer_pick = random.randint(0, 2)
  
  print(f"Computer Chose: {option_list[computer_pick]}") #prints index from option_list variable above
  
  
  if (player_option == 0 and computer_pick == 1):
    print("You lose!")
  elif (player_option == 1 and computer_pick == 2):
    print("You lose!")
  elif (player_option == 2 and computer_pick == 0):
    print("You lose!")
  elif (player_option == computer_pick):
    print("It's a tie!")
  else:
    print("You won!")
  
  

