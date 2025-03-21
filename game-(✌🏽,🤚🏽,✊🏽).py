import random

while True:
 items = ["rock","paper","scissors"]
 bot = random.choice(items)
 player = None
 while player not in items: 
   player = input("choose 'rock'or'paper'or'scissors':                 ").lower()
 if player == bot:
  print("PLAYER: " + player)
  print("BOT: " + bot)
  print("Tie!🤝")
 elif player == "rock":
   if bot == "paper":
    print("PLAYER: " + player)
    print("BOT: " + bot)
    print("You lose❌")
   if bot == "scissors":
    print("PLAYER: " + player)
    print("BOT: " + bot)
    print("You win!✅")
 elif player == "paper":
   if bot == "scissors":
    print("PLAYER: " + player)
    print("BOT: " + bot)
    print("You lose❌")
   if bot == "rock":
    print("PLAYER: " + player)
    print("BOT: " + bot)
    print("You win!✅")
 elif player == "scissors":
   if bot == "rock":
    print("PLAYER: " + player)
    print("BOT: " + bot)
    print("You lose!❌")
   if bot == "paper":
    print("PLAYER: " + player)
    print("BOT: " + bot)
    print("You win!✅")
 play_again = input("Play again? (yes/no): ").lower()
 if play_again !="yes":
     break 
print("bye!👋🏽")
