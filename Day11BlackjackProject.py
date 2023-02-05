############### Blackjack Project #####################
############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import *
import random
from replit import clear



def deal_card(): #Returns a random card from deck
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card



def calculate_score(cards): #Takes a list of cards and return the score calculated from the cards
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, cpu_score): #compares the user's score and cpu score
  if user_score == cpu_score:
    return "It's a tie!"
  elif cpu_score == 0:
    return "You lost. The CPU has Blackjack!"
  elif user_score == 0:
    return "You won. You have Blackjack!"
  elif user_score > 21:
    return "You went over 21. You lose."
  elif cpu_score > 21:
    return "CPU went over 21. You won!."
  elif user_score > cpu_score:
    return "You have the higher score. You win!"
  else:
    return "You lose."


def play_game(): #function to play the game

  print(logo) #prints logo before start of every game
  
  user_cards = [] #new list for cards that will be drawn
  computer_cards = []
  is_game_over = False

  
  for x in range(2): #will only loop 2 times total
    user_cards.append(deal_card()) #adds 2 new cards to the user for the game
    computer_cards.append(deal_card()) #adds 1 card to the computer's hand
  
  
  while not is_game_over: #loop for the user player to keep playing
    user_score = calculate_score(user_cards)
    cpu_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score} ")
    print(f"Computer's first card: {computer_cards[0]} \n")
    
    if user_score == 0 or user_score > 21 or cpu_score == 0: #if user/cpu score is 0 or user score is over 21, the game should end
      is_game_over = True
    else:
      draw_again = input("Would you like to draw another card? 'y' for yes and 'n' to pass. \n")
      if draw_again == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
    
  

  while cpu_score != 0 and cpu_score < 17: #while computer's score is not 0 and less than 17, draw another card
    computer_cards.append(deal_card()) #adds card to computer_cards list
    cpu_score = calculate_score(computer_cards) #calculates the score of the cpu
  
  
  print(f"Your final hand is {user_cards}  Final score: {user_score} ")
  print(f"Computer's final hand: {computer_cards}  CPU score: {cpu_score} \n")
  print(compare(user_score, cpu_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y': #loops the game while asking user if they want to play
  clear()
  play_game()
  


