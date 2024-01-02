import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_choices(user_choice, computer_choice):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

user_score = 0
computer_score = 0

while True:
    print("\nRock, Paper, Scissors Game:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    try:
        user_choice_num = int(input("Enter your choice (1-4): "))
        if user_choice_num == 4:
            print("\nGame over. Final scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            break
        elif user_choice_num < 1 or user_choice_num > 3:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    choices = ['rock', 'paper', 'scissors']
    user_choice = choices[user_choice_num - 1]
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)
    display_choices(user_choice, computer_choice)
    print(result)

    if 'win' in result:
        user_score += 1
    elif 'lose' in result:
        computer_score += 1

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("\nGame over. Final scores:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        break
