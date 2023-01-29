from art import *

#Calculator operation functions
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = { #dictionary
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator(): #calculator function
  print(logo)
  num1 = float(input("\nWhat's the first number? "))
  
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue: #loops until user chooses to stop it
  
    operation_symbol = input("\nPick an operation: \n")
    
    num2 = float(input("What's the next number? "))
    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"\n{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator() #recursion, calls calculator function after user decides to stop

calculator() #calculator function call
  
  
  
