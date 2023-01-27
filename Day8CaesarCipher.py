
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet: #checks if char in start_text is in alphabet list
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char #if char is a number or symbol, then just add it and don't change it since it's not in alphabet list

    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    
  print(f"\nHere's the {cipher_direction}d result: {end_text}\n")


from art import *
print(logo)



should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26 #if shift number is a large number, then just get the remainder of it after dividing by 26, and shift it by that amount
    
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  decision = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if decision == 'no':
    should_continue = False
    print("\nGoodbye!")
    
    
    
