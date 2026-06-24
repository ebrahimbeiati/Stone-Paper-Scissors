import random

def decide_winner(player, computer):
    print(f"User choice: {player}  Computer choice: {computer}")

    if player == 1 and computer == 3:
        return "You win"
    elif player == 2 and computer == 1:
       return "You win"
    elif player == 3 and computer == 2:
        return "You win"
    elif player == computer:
        return "Tie again"
    else:
        return "Computer win" 
def play_game():
    user_input = input("\nPlease enter a numbers: \n1 : Stone \n2 : Paper \n3 : Scissors\n\n")

    if user_input.lower() == "quit":
        return 
    
    if user_input not in ["1", "2", "3"]:
        print("You must enter numbers between 1,2 or 3")
        return play_game()
    
    user_choice = int(user_input)
    computer_choice = int(random.choice("123"))

    game_result = decide_winner(user_choice, computer_choice)
    print(game_result)
    return play_game()

play_game()