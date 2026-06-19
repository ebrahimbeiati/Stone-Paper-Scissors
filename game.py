import sys
import random

user_input = input("\nPlease enter a numbers: \n1 : Stone \n2 : Paper \n3 : Scissors\n\n")

if user_input.isdigit():
    user_choice = int(user_input)
    if(user_choice < 0 or user_choice > 3):
        print("You must enter 1 or 2 or 3")
        sys.exit()
else:
    print("Invalid input. Please enter a number.")
    sys.exit()
computer_value = int(random.choice("123"))
computer_choice = input(computer_value)
print(f"User choice: {user_input}  Computer choice: {computer_value}")


if user_choice == 1 and computer_choice == 3:
    print("You win")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif user_choice == 3 and computer_choice == 2:
    print("You win")
elif user_choice == computer_choice:
        print("Tie again")
else:
        print("Computer win") 