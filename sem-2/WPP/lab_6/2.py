import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.user_score = 0
        self.computer_score = 0

    def computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def play_round(self, user_choice):
        self.current_round += 1
        computer_choice = self.computer_choice()

        if user_choice == computer_choice:
            result = "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "user"
            self.user_score += 1
        else:
            result = "computer"
            self.computer_score += 1

        print(f"You chose: {user_choice}, Computer chose: {computer_choice}")
        print(f"Winner: {result}\n")

    def is_game_over(self):
        return self.current_round >= self.rounds

    def final_winner(self):
        if self.user_score > self.computer_score:
            return "You win"
        elif self.computer_score > self.user_score:
            return "Computer wins"
        else:
            return "It's a tie"
#no of games
game = RockPaperScissors(3)

while not game.is_game_over():
    while True:
        user_move = input("Enter rock, paper, or scissors: ").lower()
        if user_move in ["rock", "paper", "scissors"]:
            break
        print("Invalid choice, try again.")

    game.play_round(user_move)

print("\n--- Final Results ---")
print(f"User: {game.user_score}, Computer: {game.computer_score}")
print(game.final_winner())
