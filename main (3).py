def main_menu(choice):
  print('Welcome to Math Quiz')
  print('1. Adding Random Numbers')
  print('2. Subtracting Random Numbers')
  print('3. Exit')

main_menu('choice')
choice = int(input('Please choose one of the menu options: '))
def random_number():
  import random
  number1 = random.randint(1,10)
  number2 = random.randint(1,10)
  print(' ', number1)
  print('+', number2)
  num = number1 + number2
  ans = int(input('Enter answer.\n'))
  guess = 0
  while num!= ans:
      if ans < num:
         print("Too low")
         ans = int(input("Enter number again: "))
         guess+= 1

      elif ans > num:
         print("Too high!")
         ans = int(input("Enter number again: "))
         guess+= 1
  
  if ans == num:
    print("you guessed it right!!")
    guess+= 1
    print('Number of guesses: ', guess)

def sub_ran_num():
  import random
  num = 0
  guess = 0
  answer = 0
  number1 = random.randint(1,10)
  number2 = random.randint(1,10)
  print(' ', number1)
  print('-', number2)
  num = number1 - number2
  answer = int(input('What is the anwer?.\n'))
  while num!= answer:
      if answer < num:
         print("Too low")
         answer = int(input("Enter number again: "))
         guess+= 1

      elif answer > num:
         print("Too high!")
         answer = int(input("Enter number again: "))
         guess+= 1
  
  if answer == num:
    print("you guessed it right!!")
    guess+= 1
    print('Number of guesses: ', guess)

#if statements to determine what happens
while choice != 3:
  if choice == 1:
    random_number()
    main_menu('choice')
    choice = int(input('Please choose one of the menu options: '))
  
  elif choice == 2:
    sub_ran_num()
    main_menu('choice')
    choice = int(input('Please choose one of the menu options: '))
if choice == 3:
    print('Thank you for playing! Bye!!!!')
